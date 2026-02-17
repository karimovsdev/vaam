# Production Server Deployment - Client Data

## Müştəri Məlumatlarının Production Server-ə Əlavə Edilməsi

Bu təlimat müştəri tərəfindən verilən məlumatların production server-də database-ə əlavə edilməsi üçün hazırlanmışdır.

---

## 📋 Əlavə Olunan Məlumatlar

### 1. **Site Settings** (Sayt Tənzimləmələri)
- Şirkət adı: VAAM Import and Export Trading Co., LTD
- Telefon: +8618690149671, +8615026032721
- Email: 2776792683@qq.com, 1424705454@qq.com
- Ünvan: Room 688, 103 Huanshi West Road, Liwan District, Guangzhou
- 4 dildə tərcümə: EN, RU, TR, AR

### 2. **Hero Slide** (Əsas Banner)
- Başlıq: "Your Reliable Trading Partner in China"
- Alt başlıq: "We Find, Select and Supply Products"
- 4 dildə tam tərcümə

### 3. **Company Info** (Şirkət Haqqında)
- Şirkət təsviri
- **Mission** (Missiya): Çində etibarlı təchizat platforması yaratmaq
- **Vision** (Vizyon): Beynəlxalq ticarətdə tanınan regional brend olmaq
- **Values** (Dəyərlər): 6 əsas dəyər
- **History** (Tarixçə): 2023-2025 arası inkişaf tarixi
- 4 dildə tam tərcümə

### 4. **Company Features** (Güclü Tərəflər) - 6 ədəd
1. Etibarlı Təchizatçı Şəbəkəsi
2. Fərdi Sifariş və Təchizat Xidməti
3. Sürətli və Operativ İş Prosesi
4. Müştəri Məmnuniyyətinə Fokus
5. Geniş Məhsul Portfeli
6. Şəffaflıq və Keyfiyyət Zəmanəti

### 5. **Statistics** (Rəqəmlər) - 5 ədəd
- 50+ Tamamlanmış Layihə
- 30+ Məmnun Müştəri
- 1+ İl Təcrübə
- 5 MW+ Quraşdırılmış Güc
- 3+ Əhatə Olunan Ölkələr

### 6. **Product Categories** (Məhsul Kateqoriyaları) - 6 ədəd
1. Günəş Panelləri
2. Yol və Bağ İşıqlandırması
3. Təhlükəsizlik Kameraları
4. Avtomobillər
5. Tikinti Materialları
6. Sənaye Məhsulları

### 7. **Process Steps** (İş Prosesi) - 6 addım
1. Məsləhət və Sifarişin Qəbulu
2. Məhsul Araşdırması və Seçimi
3. Təchizat və İdxal
4. Keyfiyyət Yoxlaması
5. Çatdırılma və Quraşdırma Dəstəyi
6. Satış Sonrası Xidmət

### 8. **FAQs** (Tez-tez Soruşulan Suallar) - 8 ədəd
- Sifariş necə verilir?
- Çatdırılma müddəti nə qədərdir?
- Keyfiyyət zəmanəti varmı?
- Xarici ölkələrə göndərmə?
- Fərdi layihələr üçün xidmət?
- Texniki dəstək?
- Qiymətlərin müəyyənləşdirilməsi
- Əvvəlcədən məsləhət

### 9. **News** (Xəbərlər) - 1 nümunə
- "New Street and Garden Lighting Projects"

---

## 🚀 Production Server-də İcra Edilməsi

### Variant 1: SSH ilə birbaşa əmr (Tövsiyə olunan)

```bash
# 1. Server-ə qoşul
ssh user@your-server-ip

# 2. Layihə qovluğuna keç
cd /home/vaam/app

# 3. Seed skriptini yerləşdir (local-dan server-ə)
# Local kompüterdə ayrı terminalda:
scp seed_client_data.py user@your-server-ip:/home/vaam/app/

# 4. Virtual environment aktivləşdir və skripti işlət
source venv/bin/activate
python seed_client_data.py

# və ya Django shell vasitəsilə:
python manage.py shell < seed_client_data.py
```

### Variant 2: Git vasitəsilə

```bash
# 1. Local-da commit et
git add seed_client_data.py
git commit -m "Add client data seed script"
git push origin main

# 2. Server-də pull et
ssh user@your-server-ip
cd /home/vaam/app
git pull origin main

# 3. Skripti işlət
source venv/bin/activate
python seed_client_data.py
```

### Variant 3: FTP/SFTP vasitəsilə

1. FileZilla və ya WinSCP ilə `seed_client_data.py` faylını server-ə yüklə
2. SSH ilə server-ə qoşul
3. Skripti işlət

---

## ✅ Yoxlama

Skript işlədikdən sonra yoxlamaq üçün:

```bash
# Django shell-də yoxla
python manage.py shell

# Shell-də:
from core.models import SiteSettings, CompanyFeature, ProductCategory, FAQ
print(f"Site name: {SiteSettings.get_settings().site_name_en}")
print(f"Features: {CompanyFeature.objects.count()}")
print(f"Categories: {ProductCategory.objects.count()}")
print(f"FAQs: {FAQ.objects.count()}")
```

Və ya admin paneldən yoxla:
- https://your-domain.com/admin/
- Login ol
- Core > Site Settings, Company Features, Statistics, Product Categories, FAQs bölmələrini yoxla

---

## 🗑️ Əgər məlumatları silmək lazım olarsa

Skript yenidən işləməzdən əvvəl köhnə məlumatları silir, ancaq manual silmək üçün:

```bash
python manage.py shell

# Shell-də:
from core.models import CompanyFeature, Statistic, ProductCategory, ProcessStep, FAQ
CompanyFeature.objects.all().delete()
Statistic.objects.all().delete()
ProductCategory.objects.all().delete()
ProcessStep.objects.all().delete()
FAQ.objects.all().delete()
```

---

## 📝 Qeydlər

- **Bütün məlumatlar 4 dildə**: İngilis (EN), Rus (RU), Türk (TR), Ərəb (AR)
- **Tərcümələr peşəkar səviyyədə**: Modeltranslation vasitəsilə idarə olunur
- **Database migration tələb olunmur**: Mövcud model strukturu istifadə olunur
- **Təhlükəsiz**: Skript yalnızca müştəri məlumatlarını əlavə edir, mövcud məlumatları dəyişdirmir (yalnız Site Settings və Company Info yenilənir)

---

## 🆘 Problem Həlli

### "ModuleNotFoundError: No module named 'modeltranslation'"
```bash
pip install django-modeltranslation
# və ya
pip install -r requirements.txt
```

### "No such file or directory: seed_client_data.py"
Faylın düzgün yerdə olduğundan əmin ol:
```bash
ls -la seed_client_data.py
```

### Virtual environment aktivləşməyib
```bash
which python  # yoxla
source venv/bin/activate  # aktivləşdir
which python  # yenidən yoxla
```

---

## 📞 Əlaqə

Hər hansı problem yaranarsa, development komandası ilə əlaqə saxlayın.

---

**Son yeniləmə:** 2026-02-17
**Versiya:** 1.0
