"""
Seed script: Project data based on data_new.md
Adds real delivery projects (generators to AZ+UZ, transformers to AZ+RU)
with 4-language support and multiple images per project.

Run: /home/vaam/app/venv/bin/python3 /home/vaam/app/seed_projects.py
"""
import os
import django
import urllib.request
import urllib.error
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vaam_project.settings')
django.setup()

from core.models import ProjectCategory, Project, ProjectImage

# ─── Image download helper ────────────────────────────────────────────────────

MEDIA_ROOT = '/home/vaam/app/media'

WIKIMEDIA = 'https://upload.wikimedia.org/wikipedia/commons/'

IMAGES = {
    # key: (relative_path, url)
    'gen-az-main':     ('projects/gen-az-main.jpg',        WIKIMEDIA + 'd/dc/Diesel_Generators.jpg'),
    'gen-az-1':        ('projects/gallery/gen-az-1.jpg',   WIKIMEDIA + 'e/e0/Cumminspower.jpg'),
    'gen-az-2':        ('projects/gallery/gen-az-2.jpg',   WIKIMEDIA + 'f/f6/Caterpillar_%28Olympian%29_Generator_Set.jpg'),
    'gen-az-3':        ('projects/gallery/gen-az-3.jpg',   WIKIMEDIA + '8/8d/BRS_40_kVA_generator.jpg'),
    'gen-uz-main':     ('projects/gen-uz-main.jpg',        WIKIMEDIA + 'e/e0/Cumminspower.jpg'),
    'gen-uz-1':        ('projects/gallery/gen-uz-1.jpg',   WIKIMEDIA + 'd/dc/Diesel_Generators.jpg'),
    'gen-uz-2':        ('projects/gallery/gen-uz-2.jpg',   WIKIMEDIA + '3/3d/PJD_Genset_700kva.jpg'),
    'gen-uz-3':        ('projects/gallery/gen-uz-3.jpg',   WIKIMEDIA + 'b/bf/Montreal_power_backup.jpg'),
    'tr-az-2500-main': ('projects/tr-az-2500-main.jpg',    WIKIMEDIA + '3/35/Budakeszitrafo.JPG'),
    'tr-az-2500-1':    ('projects/gallery/tr-az-2500-1.jpg', WIKIMEDIA + 'c/c1/High-voltage_transformer.jpg'),
    'tr-az-2500-2':    ('projects/gallery/tr-az-2500-2.jpg', WIKIMEDIA + '3/35/Budakeszitrafo.JPG'),
    'tr-az-1600-main': ('projects/tr-az-1600-main.jpg',    WIKIMEDIA + 'c/c1/High-voltage_transformer.jpg'),
    'tr-az-1600-1':    ('projects/gallery/tr-az-1600-1.jpg', WIKIMEDIA + '3/35/Budakeszitrafo.JPG'),
    'tr-az-1600-2':    ('projects/gallery/tr-az-1600-2.jpg', WIKIMEDIA + 'c/c1/High-voltage_transformer.jpg'),
    'tr-ru-main':      ('projects/tr-ru-main.jpg',         WIKIMEDIA + '3/35/Budakeszitrafo.JPG'),
    'tr-ru-1':         ('projects/gallery/tr-ru-1.jpg',    WIKIMEDIA + 'c/c1/High-voltage_transformer.jpg'),
    'tr-ru-2':         ('projects/gallery/tr-ru-2.jpg',    WIKIMEDIA + '3/35/Budakeszitrafo.JPG'),
}


def download_images():
    os.makedirs(os.path.join(MEDIA_ROOT, 'projects', 'gallery'), exist_ok=True)
    headers = {'User-Agent': 'Mozilla/5.0'}
    for key, (rel_path, url) in IMAGES.items():
        dest = os.path.join(MEDIA_ROOT, rel_path)
        if os.path.exists(dest) and os.path.getsize(dest) > 0:
            print(f'  [skip] {rel_path}')
            continue
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as resp, open(dest, 'wb') as f:
                f.write(resp.read())
            print(f'  [ok]   {rel_path}')
        except Exception as e:
            print(f'  [err]  {rel_path}: {e}')


# ─── Category helper ─────────────────────────────────────────────────────────

def get_or_create_category(slug, name_en, name_ru, name_tr, name_ar, order):
    cat, created = ProjectCategory.objects.get_or_create(
        slug=slug,
        defaults={'order': order}
    )
    cat.name_en = name_en
    cat.name_ru = name_ru
    cat.name_tr = name_tr
    cat.name_ar = name_ar
    cat.order = order
    cat.is_active = True
    cat.save()
    print(f"  {'Created' if created else 'Updated'} category: {name_en}")
    return cat


# ─── Project upsert helper ────────────────────────────────────────────────────

def upsert_project(slug, category, fields, gallery_images):
    """Create or update a project + its gallery images."""
    obj, created = Project.objects.get_or_create(
        slug=slug,
        defaults={'category': category, 'image': fields.get('image', '')}
    )
    for k, v in fields.items():
        setattr(obj, k, v)
    obj.category = category
    obj.is_active = True
    obj.save()
    print(f"  {'Created' if created else 'Updated'} project: {fields.get('title_en')}")

    # Replace gallery images
    obj.images.all().delete()
    for order, (rel_path, alt_en) in enumerate(gallery_images, start=1):
        if os.path.exists(os.path.join(MEDIA_ROOT, rel_path)):
            ProjectImage.objects.create(
                project=obj,
                image=rel_path,
                alt_text=alt_en,
                order=order,
            )
    return obj


# ─── Main ────────────────────────────────────────────────────────────────────

print('\n=== Downloading images ===')
download_images()

print('\n=== Project categories ===')
cat_gen = get_or_create_category(
    slug='generator-supply',
    name_en='Generator Supply',
    name_ru='Поставка генераторов',
    name_tr='Jeneratör Tedariki',
    name_ar='توريد المولدات',
    order=1,
)
cat_tr = get_or_create_category(
    slug='transformer-supply',
    name_en='Distribution Transformer Supply',
    name_ru='Поставка распределительных трансформаторов',
    name_tr='Dağıtım Transformatörü Tedariki',
    name_ar='توريد محولات التوزيع',
    order=2,
)

print('\n=== Projects ===')

# ── 1. Generators → Azerbaijan ────────────────────────────────────────────────
upsert_project(
    slug='generator-supply-azerbaijan-2022-2025',
    category=cat_gen,
    fields=dict(
        title_en='Diesel Generator Supply – Republic of Azerbaijan',
        title_ru='Поставка дизельных генераторов – Азербайджанская Республика',
        title_tr='Dizel Jeneratör Tedariki – Azerbaycan Cumhuriyeti',
        title_ar='توريد مولدات الديزل – جمهورية أذربيجان',

        short_description_en='Supply of 50–500 kVA diesel generators to the Republic of Azerbaijan. Delivered between 2022 and 2025.',
        short_description_ru='Поставка дизельных генераторов мощностью 50–500 кВА в Азербайджанскую Республику. Поставки осуществлены в период 2022–2025 гг.',
        short_description_tr='Azerbaycan Cumhuriyeti\'ne 50–500 kVA dizel jeneratör tedariki. 2022–2025 yılları arasında teslim edilmiştir.',
        short_description_ar='توريد مولدات ديزل بقدرة 50–500 كيلوفولت أمبير إلى جمهورية أذربيجان. تم التسليم خلال الفترة 2022–2025.',

        description_en='''<p>VAAM (Guangzhou) Import and Export Trading Co., Ltd. successfully delivered a series of diesel generator sets to the Republic of Azerbaijan between 2022 and 2025.</p>
<p><strong>Delivered Units:</strong></p>
<ul>
<li>50 kVA Diesel Generator</li>
<li>100 kVA Diesel Generator</li>
<li>150 kVA Diesel Generator</li>
<li>300 kVA Diesel Generator</li>
<li>375 kVA Diesel Generator</li>
<li>500 kVA Diesel Generator</li>
</ul>
<p><strong>Delivery Timeline:</strong> 25–40 days per shipment</p>
<p>All units were delivered with full technical documentation, factory test reports, and customs clearance support.</p>''',

        description_ru='''<p>VAAM (Guangzhou) Import and Export Trading Co., Ltd. успешно осуществила поставку серии дизельных генераторных установок в Азербайджанскую Республику в период с 2022 по 2025 год.</p>
<p><strong>Поставленные единицы:</strong></p>
<ul>
<li>Дизельный генератор 50 кВА</li>
<li>Дизельный генератор 100 кВА</li>
<li>Дизельный генератор 150 кВА</li>
<li>Дизельный генератор 300 кВА</li>
<li>Дизельный генератор 375 кВА</li>
<li>Дизельный генератор 500 кВА</li>
</ul>
<p><strong>Срок доставки:</strong> 25–40 дней на партию</p>
<p>Все агрегаты были поставлены с полной технической документацией, заводскими протоколами испытаний и поддержкой таможенного оформления.</p>''',

        description_tr='''<p>VAAM (Guangzhou) Import and Export Trading Co., Ltd., 2022–2025 yılları arasında Azerbaycan Cumhuriyeti\'ne bir dizi dizel jeneratör seti başarıyla teslim etmiştir.</p>
<p><strong>Teslim Edilen Birimler:</strong></p>
<ul>
<li>50 kVA Dizel Jeneratör</li>
<li>100 kVA Dizel Jeneratör</li>
<li>150 kVA Dizel Jeneratör</li>
<li>300 kVA Dizel Jeneratör</li>
<li>375 kVA Dizel Jeneratör</li>
<li>500 kVA Dizel Jeneratör</li>
</ul>
<p><strong>Teslimat Süresi:</strong> Sevkiyat başına 25–40 gün</p>
<p>Tüm üniteler tam teknik dokümantasyon, fabrika test raporları ve gümrük işlemleri desteğiyle teslim edilmiştir.</p>''',

        description_ar='''<p>نجحت شركة VAAM (Guangzhou) Import and Export Trading Co., Ltd. في تسليم سلسلة من مجموعات مولدات الديزل إلى جمهورية أذربيجان خلال الفترة من 2022 إلى 2025.</p>
<p><strong>الوحدات المسلمة:</strong></p>
<ul>
<li>مولد ديزل 50 كيلوفولت أمبير</li>
<li>مولد ديزل 100 كيلوفولت أمبير</li>
<li>مولد ديزل 150 كيلوفولت أمبير</li>
<li>مولد ديزل 300 كيلوفولت أمبير</li>
<li>مولد ديزل 375 كيلوفولت أمبير</li>
<li>مولد ديزل 500 كيلوفولت أمبير</li>
</ul>
<p><strong>مدة التسليم:</strong> 25–40 يومًا لكل شحنة</p>
<p>تم تسليم جميع الوحدات مع الوثائق التقنية الكاملة وتقارير الاختبار وخدمات التخليص الجمركي.</p>''',

        client_en='Republic of Azerbaijan',
        client_ru='Азербайджанская Республика',
        client_tr='Azerbaycan Cumhuriyeti',
        client_ar='جمهورية أذربيجان',

        location_en='Baku, Azerbaijan',
        location_ru='Баку, Азербайджан',
        location_tr='Bakü, Azerbaycan',
        location_ar='باكو، أذربيجان',

        image='projects/gen-az-main.jpg',
        date_completed=date(2025, 12, 31),
        is_featured=True,
        order=1,
    ),
    gallery_images=[
        ('projects/gallery/gen-az-1.jpg', '150 kVA Cummins Diesel Generator – Azerbaijan'),
        ('projects/gallery/gen-az-2.jpg', '200 kW Caterpillar Generator Set'),
        ('projects/gallery/gen-az-3.jpg', '50 kVA Diesel Generator – Delivery'),
    ],
)

# ── 2. Generators → Uzbekistan ────────────────────────────────────────────────
upsert_project(
    slug='generator-supply-uzbekistan-2022-2025',
    category=cat_gen,
    fields=dict(
        title_en='Diesel Generator Supply – Republic of Uzbekistan',
        title_ru='Поставка дизельных генераторов – Республика Узбекистан',
        title_tr='Dizel Jeneratör Tedariki – Özbekistan Cumhuriyeti',
        title_ar='توريد مولدات الديزل – جمهورية أوزبكستان',

        short_description_en='Supply of 50–500 kVA diesel generators to the Republic of Uzbekistan. Delivered between 2022 and 2025.',
        short_description_ru='Поставка дизельных генераторов мощностью 50–500 кВА в Республику Узбекистан. Поставки осуществлены в период 2022–2025 гг.',
        short_description_tr='Özbekistan Cumhuriyeti\'ne 50–500 kVA dizel jeneratör tedariki. 2022–2025 yılları arasında teslim edilmiştir.',
        short_description_ar='توريد مولدات ديزل بقدرة 50–500 كيلوفولت أمبير إلى جمهورية أوزبكستان. تم التسليم خلال الفترة 2022–2025.',

        description_en='''<p>VAAM (Guangzhou) Import and Export Trading Co., Ltd. successfully completed the export and delivery of diesel generator sets to the Republic of Uzbekistan over the period 2022–2025.</p>
<p><strong>Delivered Units:</strong></p>
<ul>
<li>50 kVA Diesel Generator</li>
<li>100 kVA Diesel Generator</li>
<li>150 kVA Diesel Generator</li>
<li>300 kVA Diesel Generator</li>
<li>375 kVA Diesel Generator</li>
<li>500 kVA Diesel Generator</li>
</ul>
<p><strong>Delivery Timeline:</strong> 25–40 days per shipment</p>
<p>Shipments included full customs documentation and technical support upon arrival.</p>''',

        description_ru='''<p>VAAM (Guangzhou) Import and Export Trading Co., Ltd. успешно завершила экспорт и поставку дизельных генераторных установок в Республику Узбекистан в период 2022–2025 гг.</p>
<p><strong>Поставленные единицы:</strong></p>
<ul>
<li>Дизельный генератор 50 кВА</li>
<li>Дизельный генератор 100 кВА</li>
<li>Дизельный генератор 150 кВА</li>
<li>Дизельный генератор 300 кВА</li>
<li>Дизельный генератор 375 кВА</li>
<li>Дизельный генератор 500 кВА</li>
</ul>
<p><strong>Срок доставки:</strong> 25–40 дней на партию</p>
<p>Поставки включали полную таможенную документацию и техническую поддержку по прибытии.</p>''',

        description_tr='''<p>VAAM (Guangzhou) Import and Export Trading Co., Ltd., 2022–2025 yılları arasında Özbekistan Cumhuriyeti\'ne dizel jeneratör setlerinin ihracat ve teslimatını başarıyla tamamlamıştır.</p>
<p><strong>Teslim Edilen Birimler:</strong></p>
<ul>
<li>50 kVA Dizel Jeneratör</li>
<li>100 kVA Dizel Jeneratör</li>
<li>150 kVA Dizel Jeneratör</li>
<li>300 kVA Dizel Jeneratör</li>
<li>375 kVA Dizel Jeneratör</li>
<li>500 kVA Dizel Jeneratör</li>
</ul>
<p><strong>Teslimat Süresi:</strong> Sevkiyat başına 25–40 gün</p>
<p>Sevkiyatlar tam gümrük belgelendirmesi ve varış sonrası teknik destek içermekteydi.</p>''',

        description_ar='''<p>نجحت شركة VAAM (Guangzhou) Import and Export Trading Co., Ltd. في إتمام عمليات تصدير وتسليم مجموعات مولدات الديزل إلى جمهورية أوزبكستان خلال الفترة من 2022 إلى 2025.</p>
<p><strong>الوحدات المسلمة:</strong></p>
<ul>
<li>مولد ديزل 50 كيلوفولت أمبير</li>
<li>مولد ديزل 100 كيلوفولت أمبير</li>
<li>مولد ديزل 150 كيلوفولت أمبير</li>
<li>مولد ديزل 300 كيلوفولت أمبير</li>
<li>مولد ديزل 375 كيلوفولت أمبير</li>
<li>مولد ديزل 500 كيلوفولت أمبير</li>
</ul>
<p><strong>مدة التسليم:</strong> 25–40 يومًا لكل شحنة</p>
<p>تضمنت الشحنات الوثائق الجمركية الكاملة والدعم الفني عند الوصول.</p>''',

        client_en='Republic of Uzbekistan',
        client_ru='Республика Узбекистан',
        client_tr='Özbekistan Cumhuriyeti',
        client_ar='جمهورية أوزبكستان',

        location_en='Tashkent, Uzbekistan',
        location_ru='Ташкент, Узбекистан',
        location_tr='Taşkent, Özbekistan',
        location_ar='طشقند، أوزبكستان',

        image='projects/gen-uz-main.jpg',
        date_completed=date(2025, 12, 31),
        is_featured=True,
        order=2,
    ),
    gallery_images=[
        ('projects/gallery/gen-uz-1.jpg', 'Perkins Diesel Generators – Uzbekistan Supply'),
        ('projects/gallery/gen-uz-2.jpg', '700 kVA Genset – Loaded for Export'),
        ('projects/gallery/gen-uz-3.jpg', 'Diesel Generator Ready for Shipment'),
    ],
)

# ── 3. Transformers 2500 kVA → Azerbaijan (Oct 2024) ─────────────────────────
upsert_project(
    slug='transformer-2500kva-supply-azerbaijan-2024',
    category=cat_tr,
    fields=dict(
        title_en='2500 kVA S11 Distribution Transformer Delivery – Azerbaijan (Oct 2024)',
        title_ru='Поставка распределительных трансформаторов S11 2500 кВА – Азербайджан (окт. 2024)',
        title_tr='2500 kVA S11 Dağıtım Transformatörü Teslimatı – Azerbaycan (Ek. 2024)',
        title_ar='تسليم محولات التوزيع S11 بقدرة 2500 كيلوفولت أمبير – أذربيجان (أكتوبر 2024)',

        short_description_en='Delivery of two S11-2500/35 distribution transformers (Aluminium and Copper windings) to Azerbaijan on 25 October 2024.',
        short_description_ru='Поставка двух распределительных трансформаторов S11-2500/35 (алюминиевая и медная обмотки) в Азербайджан 25 октября 2024 г.',
        short_description_tr='25 Ekim 2024 tarihinde Azerbaycan\'a iki adet S11-2500/35 dağıtım transformatörü (Alüminyum ve Bakır sargı) teslimatı.',
        short_description_ar='تسليم محولَي توزيع S11-2500/35 (بسارية ألومنيوم وبسارية نحاسية) إلى أذربيجان بتاريخ 25 أكتوبر 2024.',

        description_en='''<p>On <strong>25 October 2024</strong>, VAAM (Guangzhou) Import and Export Trading Co., Ltd. successfully delivered S11-series three-phase oil-immersed distribution transformers to the Republic of Azerbaijan.</p>
<p><strong>Delivered Equipment:</strong></p>
<ul>
<li>S11-2500/35 – 2500 kVA, 35/0.4 kV Distribution Transformer (Aluminium winding)</li>
<li>S11-2500/35 – 2500 kVA, 35/0.4 kV Distribution Transformer (Copper winding)</li>
</ul>
<p><strong>Technical Specifications:</strong></p>
<ul>
<li>Rated Power: 2500 kVA</li>
<li>Voltage Ratio: 35 kV / 0.4 kV</li>
<li>Cooling Method: ONAN (Oil Natural Air Natural)</li>
<li>Standard: IEC 60076, GB 1094</li>
<li>Series: S11 – Low loss, energy-efficient design</li>
</ul>''',

        description_ru='''<p><strong>25 октября 2024 г.</strong> компания VAAM (Guangzhou) Import and Export Trading Co., Ltd. успешно поставила трёхфазные масляные распределительные трансформаторы серии S11 в Азербайджанскую Республику.</p>
<p><strong>Поставленное оборудование:</strong></p>
<ul>
<li>S11-2500/35 – 2500 кВА, 35/0,4 кВ (алюминиевая обмотка)</li>
<li>S11-2500/35 – 2500 кВА, 35/0,4 кВ (медная обмотка)</li>
</ul>
<p><strong>Технические характеристики:</strong></p>
<ul>
<li>Номинальная мощность: 2500 кВА</li>
<li>Коэффициент трансформации: 35 кВ / 0,4 кВ</li>
<li>Метод охлаждения: ONAN</li>
<li>Стандарт: IEC 60076, GB 1094</li>
<li>Серия: S11 – малопотерная, энергоэффективная конструкция</li>
</ul>''',

        description_tr='''<p><strong>25 Ekim 2024</strong> tarihinde VAAM (Guangzhou) Import and Export Trading Co., Ltd., Azerbaycan Cumhuriyeti\'ne S11 serisi üç fazlı yağlı dağıtım transformatörlerini başarıyla teslim etmiştir.</p>
<p><strong>Teslim Edilen Ekipmanlar:</strong></p>
<ul>
<li>S11-2500/35 – 2500 kVA, 35/0,4 kV Dağıtım Transformatörü (Alüminyum sargı)</li>
<li>S11-2500/35 – 2500 kVA, 35/0,4 kV Dağıtım Transformatörü (Bakır sargı)</li>
</ul>
<p><strong>Teknik Özellikler:</strong></p>
<ul>
<li>Nominal Güç: 2500 kVA</li>
<li>Gerilim Oranı: 35 kV / 0,4 kV</li>
<li>Soğutma Yöntemi: ONAN</li>
<li>Standart: IEC 60076, GB 1094</li>
<li>Seri: S11 – Düşük kayıplı, enerji verimli tasarım</li>
</ul>''',

        description_ar='''<p>في <strong>25 أكتوبر 2024</strong>، نجحت شركة VAAM (Guangzhou) Import and Export Trading Co., Ltd. في تسليم محولات التوزيع ثلاثية الأوجه المغمورة بالزيت من سلسلة S11 إلى جمهورية أذربيجان.</p>
<p><strong>المعدات المسلمة:</strong></p>
<ul>
<li>S11-2500/35 – 2500 كيلوفولت أمبير، 35/0.4 كيلوفولت (سارية ألومنيوم)</li>
<li>S11-2500/35 – 2500 كيلوفولت أمبير، 35/0.4 كيلوفولت (سارية نحاسية)</li>
</ul>
<p><strong>المواصفات التقنية:</strong></p>
<ul>
<li>القدرة الاسمية: 2500 كيلوفولت أمبير</li>
<li>نسبة الجهد: 35 كيلوفولت / 0.4 كيلوفولت</li>
<li>طريقة التبريد: ONAN</li>
<li>المعيار: IEC 60076، GB 1094</li>
<li>السلسلة: S11 – تصميم منخفض الخسائر وفعّال في استهلاك الطاقة</li>
</ul>''',

        client_en='Republic of Azerbaijan',
        client_ru='Азербайджанская Республика',
        client_tr='Azerbaycan Cumhuriyeti',
        client_ar='جمهورية أذربيجان',

        location_en='Azerbaijan',
        location_ru='Азербайджан',
        location_tr='Azerbaycan',
        location_ar='أذربيجان',

        image='projects/tr-az-2500-main.jpg',
        date_completed=date(2024, 10, 25),
        is_featured=True,
        order=3,
    ),
    gallery_images=[
        ('projects/gallery/tr-az-2500-1.jpg', '2500 kVA Oil-Immersed Transformer – Copper Winding'),
        ('projects/gallery/tr-az-2500-2.jpg', '2500 kVA S11 Transformer – Azerbaijan Delivery'),
    ],
)

# ── 4. Transformers 1600 kVA → Azerbaijan (Nov 2025) ─────────────────────────
upsert_project(
    slug='transformer-1600kva-supply-azerbaijan-2025',
    category=cat_tr,
    fields=dict(
        title_en='1600 kVA S11 Distribution Transformer Delivery – Azerbaijan (Nov 2025)',
        title_ru='Поставка распределительных трансформаторов S11 1600 кВА – Азербайджан (ноябрь 2025)',
        title_tr='1600 kVA S11 Dağıtım Transformatörü Teslimatı – Azerbaycan (Kas. 2025)',
        title_ar='تسليم محولات التوزيع S11 بقدرة 1600 كيلوفولت أمبير – أذربيجان (نوفمبر 2025)',

        short_description_en='Delivery of two 1600 kVA, 35/0.4 kV distribution transformers (Aluminium and Copper windings) to Azerbaijan on 18 November 2025.',
        short_description_ru='Поставка двух распределительных трансформаторов в Азербайджан 18 ноября 2025 г.: 1600 кВА, 35/0,4 кВ (алюминиевая и медная обмотки).',
        short_description_tr='18 Kasım 2025 tarihinde Azerbaycan\'a iki adet 1600 kVA, 35/0,4 kV dağıtım transformatörü (Alüminyum ve Bakır sargı) teslimatı.',
        short_description_ar='تسليم محولَي توزيع بقدرة 1600 كيلوفولت أمبير، 35/0.4 كيلوفولت (بسارية ألومنيوم وبسارية نحاسية) إلى أذربيجان بتاريخ 18 نوفمبر 2025.',

        description_en='''<p>On <strong>18 November 2025</strong>, VAAM (Guangzhou) Import and Export Trading Co., Ltd. delivered 1600 kVA S11-series distribution transformers to the Republic of Azerbaijan.</p>
<p><strong>Delivered Equipment:</strong></p>
<ul>
<li>1600 kVA – 35/0.4 kV Distribution Transformer (Aluminium winding)</li>
<li>1600 kVA – 35/0.4 kV Distribution Transformer (Copper winding)</li>
</ul>
<p><strong>Technical Specifications:</strong></p>
<ul>
<li>Rated Power: 1600 kVA</li>
<li>Voltage Ratio: 35 kV / 0.4 kV</li>
<li>Cooling Method: ONAN (Oil Natural Air Natural)</li>
<li>Standard: IEC 60076, GB 1094</li>
<li>Series: S11 – Low loss, energy-efficient design</li>
</ul>''',

        description_ru='''<p><strong>18 ноября 2025 г.</strong> компания VAAM (Guangzhou) Import and Export Trading Co., Ltd. поставила в Азербайджанскую Республику распределительные трансформаторы серии S11 мощностью 1600 кВА.</p>
<p><strong>Поставленное оборудование:</strong></p>
<ul>
<li>1600 кВА – 35/0,4 кВ (алюминиевая обмотка)</li>
<li>1600 кВА – 35/0,4 кВ (медная обмотка)</li>
</ul>
<p><strong>Технические характеристики:</strong></p>
<ul>
<li>Номинальная мощность: 1600 кВА</li>
<li>Коэффициент трансформации: 35 кВ / 0,4 кВ</li>
<li>Метод охлаждения: ONAN</li>
<li>Стандарт: IEC 60076, GB 1094</li>
<li>Серия: S11 – малопотерная, энергоэффективная конструкция</li>
</ul>''',

        description_tr='''<p><strong>18 Kasım 2025</strong> tarihinde VAAM (Guangzhou) Import and Export Trading Co., Ltd., Azerbaycan Cumhuriyeti\'ne 1600 kVA S11 serisi dağıtım transformatörlerini teslim etmiştir.</p>
<p><strong>Teslim Edilen Ekipmanlar:</strong></p>
<ul>
<li>1600 kVA – 35/0,4 kV Dağıtım Transformatörü (Alüminyum sargı)</li>
<li>1600 kVA – 35/0,4 kV Dağıtım Transformatörü (Bakır sargı)</li>
</ul>
<p><strong>Teknik Özellikler:</strong></p>
<ul>
<li>Nominal Güç: 1600 kVA</li>
<li>Gerilim Oranı: 35 kV / 0,4 kV</li>
<li>Soğutma Yöntemi: ONAN</li>
<li>Standart: IEC 60076, GB 1094</li>
<li>Seri: S11 – Düşük kayıplı, enerji verimli tasarım</li>
</ul>''',

        description_ar='''<p>في <strong>18 نوفمبر 2025</strong>، قامت شركة VAAM (Guangzhou) Import and Export Trading Co., Ltd. بتسليم محولات التوزيع من سلسلة S11 بقدرة 1600 كيلوفولت أمبير إلى جمهورية أذربيجان.</p>
<p><strong>المعدات المسلمة:</strong></p>
<ul>
<li>1600 كيلوفولت أمبير – 35/0.4 كيلوفولت (سارية ألومنيوم)</li>
<li>1600 كيلوفولت أمبير – 35/0.4 كيلوفولت (سارية نحاسية)</li>
</ul>
<p><strong>المواصفات التقنية:</strong></p>
<ul>
<li>القدرة الاسمية: 1600 كيلوفولت أمبير</li>
<li>نسبة الجهد: 35 كيلوفولت / 0.4 كيلوفولت</li>
<li>طريقة التبريد: ONAN</li>
<li>المعيار: IEC 60076، GB 1094</li>
<li>السلسلة: S11 – تصميم منخفض الخسائر وفعّال في استهلاك الطاقة</li>
</ul>''',

        client_en='Republic of Azerbaijan',
        client_ru='Азербайджанская Республика',
        client_tr='Azerbaycan Cumhuriyeti',
        client_ar='جمهورية أذربيجان',

        location_en='Azerbaijan',
        location_ru='Азербайджан',
        location_tr='Azerbaycan',
        location_ar='أذربيجان',

        image='projects/tr-az-1600-main.jpg',
        date_completed=date(2025, 11, 18),
        is_featured=True,
        order=4,
    ),
    gallery_images=[
        ('projects/gallery/tr-az-1600-1.jpg', '1600 kVA Three-Phase Oil Transformer – Azerbaijan'),
        ('projects/gallery/tr-az-1600-2.jpg', '1600 kVA S11 Transformer – Copper Winding'),
    ],
)

# ── 5. Transformers → Russia ──────────────────────────────────────────────────
upsert_project(
    slug='transformer-supply-russia',
    category=cat_tr,
    fields=dict(
        title_en='S11 Distribution Transformer Export – Russian Federation',
        title_ru='Экспорт распределительных трансформаторов S11 – Российская Федерация',
        title_tr='S11 Dağıtım Transformatörü İhracatı – Rusya Federasyonu',
        title_ar='تصدير محولات التوزيع S11 – الاتحاد الروسي',

        short_description_en='Export of 1600 kVA and 2500 kVA, 35/0.4 kV S11-series distribution transformers (Aluminium and Copper windings) to the Russian Federation.',
        short_description_ru='Экспорт распределительных трансформаторов серии S11 мощностью 1600 кВА и 2500 кВА, 35/0,4 кВ (алюминиевая и медная обмотки) в Российскую Федерацию.',
        short_description_tr='Rusya Federasyonu\'na 1600 kVA ve 2500 kVA, 35/0,4 kV S11 serisi dağıtım transformatörü (Alüminyum ve Bakır sargı) ihracatı.',
        short_description_ar='تصدير محولات توزيع S11 بقدرة 1600 و2500 كيلوفولت أمبير، 35/0.4 كيلوفولت (بسارية ألومنيوم وبسارية نحاسية) إلى الاتحاد الروسي.',

        description_en='''<p>VAAM (Guangzhou) Import and Export Trading Co., Ltd. successfully exported S11-series three-phase oil-immersed distribution transformers to the Russian Federation.</p>
<p><strong>Exported Equipment:</strong></p>
<ul>
<li>1600 kVA – 35/0.4 kV Distribution Transformer (Aluminium winding)</li>
<li>1600 kVA – 35/0.4 kV Distribution Transformer (Copper winding)</li>
<li>2500 kVA – 35/0.4 kV Distribution Transformer (Aluminium winding)</li>
<li>2500 kVA – 35/0.4 kV Distribution Transformer (Copper winding)</li>
</ul>
<p><strong>Technical Specifications:</strong></p>
<ul>
<li>Voltage Ratio: 35 kV / 0.4 kV</li>
<li>Cooling Method: ONAN (Oil Natural Air Natural)</li>
<li>Standard: IEC 60076, GB 1094</li>
<li>Series: S11 – Low loss, energy-efficient design</li>
<li>Insulation: Oil-immersed, fully sealed</li>
</ul>''',

        description_ru='''<p>Компания VAAM (Guangzhou) Import and Export Trading Co., Ltd. успешно экспортировала трёхфазные масляные распределительные трансформаторы серии S11 в Российскую Федерацию.</p>
<p><strong>Экспортированное оборудование:</strong></p>
<ul>
<li>1600 кВА – 35/0,4 кВ (алюминиевая обмотка)</li>
<li>1600 кВА – 35/0,4 кВ (медная обмотка)</li>
<li>2500 кВА – 35/0,4 кВ (алюминиевая обмотка)</li>
<li>2500 кВА – 35/0,4 кВ (медная обмотка)</li>
</ul>
<p><strong>Технические характеристики:</strong></p>
<ul>
<li>Коэффициент трансформации: 35 кВ / 0,4 кВ</li>
<li>Метод охлаждения: ONAN</li>
<li>Стандарт: IEC 60076, GB 1094</li>
<li>Серия: S11 – малопотерная, энергоэффективная конструкция</li>
<li>Изоляция: масляная, полностью герметичная</li>
</ul>''',

        description_tr='''<p>VAAM (Guangzhou) Import and Export Trading Co., Ltd., Rusya Federasyonu\'na S11 serisi üç fazlı yağlı dağıtım transformatörlerini başarıyla ihraç etmiştir.</p>
<p><strong>İhraç Edilen Ekipmanlar:</strong></p>
<ul>
<li>1600 kVA – 35/0,4 kV Dağıtım Transformatörü (Alüminyum sargı)</li>
<li>1600 kVA – 35/0,4 kV Dağıtım Transformatörü (Bakır sargı)</li>
<li>2500 kVA – 35/0,4 kV Dağıtım Transformatörü (Alüminyum sargı)</li>
<li>2500 kVA – 35/0,4 kV Dağıtım Transformatörü (Bakır sargı)</li>
</ul>
<p><strong>Teknik Özellikler:</strong></p>
<ul>
<li>Gerilim Oranı: 35 kV / 0,4 kV</li>
<li>Soğutma Yöntemi: ONAN</li>
<li>Standart: IEC 60076, GB 1094</li>
<li>Seri: S11 – Düşük kayıplı, enerji verimli</li>
<li>Yalıtım: Yağlı, tam kapalı</li>
</ul>''',

        description_ar='''<p>نجحت شركة VAAM (Guangzhou) Import and Export Trading Co., Ltd. في تصدير محولات التوزيع ثلاثية الأوجه المغمورة بالزيت من سلسلة S11 إلى الاتحاد الروسي.</p>
<p><strong>المعدات المصدَّرة:</strong></p>
<ul>
<li>1600 كيلوفولت أمبير – 35/0.4 كيلوفولت (سارية ألومنيوم)</li>
<li>1600 كيلوفولت أمبير – 35/0.4 كيلوفولت (سارية نحاسية)</li>
<li>2500 كيلوفولت أمبير – 35/0.4 كيلوفولت (سارية ألومنيوم)</li>
<li>2500 كيلوفولت أمبير – 35/0.4 كيلوفولت (سارية نحاسية)</li>
</ul>
<p><strong>المواصفات التقنية:</strong></p>
<ul>
<li>نسبة الجهد: 35 كيلوفولت / 0.4 كيلوفولت</li>
<li>طريقة التبريد: ONAN</li>
<li>المعيار: IEC 60076، GB 1094</li>
<li>السلسلة: S11 – تصميم منخفض الخسائر وفعّال</li>
<li>العزل: مغمور بالزيت، مختوم بالكامل</li>
</ul>''',

        client_en='Russian Federation',
        client_ru='Российская Федерация',
        client_tr='Rusya Federasyonu',
        client_ar='الاتحاد الروسي',

        location_en='Russia',
        location_ru='Россия',
        location_tr='Rusya',
        location_ar='روسيا',

        image='projects/tr-ru-main.jpg',
        date_completed=None,
        is_featured=True,
        order=5,
    ),
    gallery_images=[
        ('projects/gallery/tr-ru-1.jpg', 'S11 High-Voltage Transformer – Russia Export'),
        ('projects/gallery/tr-ru-2.jpg', 'Oil-Immersed Distribution Transformer – Russian Federation'),
    ],
)

# ── Fix permissions ───────────────────────────────────────────────────────────
import subprocess
subprocess.run([
    'chown', '-R', 'vaam:www-data',
    '/home/vaam/app/media/projects'
], check=False)
subprocess.run([
    'chmod', '-R', '644',
    '/home/vaam/app/media/projects'
], check=False)
subprocess.run([
    'find', '/home/vaam/app/media/projects', '-type', 'd',
    '-exec', 'chmod', '755', '{}', ';'
], check=False)

print('\n=== All projects seeded successfully! ===')
