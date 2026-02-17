"""
VAAM - Update Menu Items with 4-Language Support
Run: python seed_menu_translations.py
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vaam_project.settings')
django.setup()

from django.utils.translation import activate
from core.models import Menu, MenuItem

print("=" * 80)
print("  VAAM - Creating Multilingual Menu")
print("=" * 80)

# Get or create Main Menu
main_menu, created = Menu.objects.get_or_create(
    slug='main',
    defaults={
        'title': 'Main Navigation',
        'location': 'main',
        'is_active': True
    }
)

# Manually set translations for Menu
main_menu.title_en = 'Main Navigation'
main_menu.title_ru = 'Главное меню'
main_menu.title_tr = 'Ana Menü'
main_menu.title_ar = 'القائمة الرئيسية'
main_menu.save()

if not created:
    print("✓ Main menu already exists - updated translations")
else:
    print("✓ Main menu created with translations")

# Delete old menu items
MenuItem.objects.filter(menu=main_menu).delete()
print("✓ Cleared old menu items")

# Menu structure with translations
menu_items = [
    {
        'order': 1,
        'link_type': 'home',
        'title_en': 'Home',
        'title_ru': 'Главная',
        'title_tr': 'Ana Sayfa',
        'title_ar': 'الرئيسية',
    },
    {
        'order': 2,
        'link_type': 'about',
        'title_en': 'About Us',
        'title_ru': 'О нас',
        'title_tr': 'Hakkımızda',
        'title_ar': 'من نحن',
    },
    {
        'order': 3,
        'link_type': 'services',
        'title_en': 'Services',
        'title_ru': 'Услуги',
        'title_tr': 'Hizmetler',
        'title_ar': 'الخدمات',
    },
    {
        'order': 4,
        'link_type': 'products',
        'title_en': 'Products',
        'title_ru': 'Продукция',
        'title_tr': 'Ürünler',
        'title_ar': 'المنتجات',
    },
    {
        'order': 5,
        'link_type': 'projects',
        'title_en': 'Projects',
        'title_ru': 'Проекты',
        'title_tr': 'Projeler',
        'title_ar': 'المشاريع',
    },
    {
        'order': 6,
        'link_type': 'news',
        'title_en': 'News',
        'title_ru': 'Новости',
        'title_tr': 'Haberler',
        'title_ar': 'الأخبار',
    },
    {
        'order': 7,
        'link_type': 'contact',
        'title_en': 'Contact',
        'title_ru': 'Контакт',
        'title_tr': 'İletişim',
        'title_ar': 'اتصل بنا',
    },
]

# Create menu items with proper modeltranslation support
created_count = 0
for item_data in menu_items:
    # Create item with English (default language)
    activate('en')
    item = MenuItem.objects.create(
        menu=main_menu,
        title=item_data['title_en'],
        link_type=item_data['link_type'],
        order=item_data['order'],
        is_active=True
    )
    
    # Update translation fields directly using update_fields
    MenuItem.objects.filter(id=item.id).update(
        title_en=item_data['title_en'],
        title_ru=item_data['title_ru'],
        title_tr=item_data['title_tr'],
        title_ar=item_data['title_ar']
    )
    
    created_count += 1
    print(f"  ✓ Created: {item_data['title_en']} / {item_data['title_ru']} / {item_data['title_tr']} / {item_data['title_ar']}")

print("\n" + "=" * 80)
print(f"  ✓ SUCCESS! Created {created_count} menu items in 4 languages")
print("=" * 80)
print("\nMenu items are now available in:")
print("  🇬🇧 English (EN)")
print("  🇷🇺 Russian (RU)")
print("  🇹🇷 Turkish (TR)")
print("  🇸🇦 Arabic (AR)")
print("\nNavbar will now show correctly in all languages!")
print("=" * 80)
