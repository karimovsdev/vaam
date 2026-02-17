"""
VAAM - Create Menu Items with 4-Language Support
Run: python seed_menu_translations.py
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vaam_project.settings')
django.setup()

from django.utils.translation import activate
from django.db import connection
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

# Update Menu translations using raw SQL
with connection.cursor() as cursor:
    cursor.execute("""
        UPDATE core_menu 
        SET title_en = %s, title_ru = %s, title_tr = %s, title_ar = %s
        WHERE id = %s
    """, ['Main Navigation', 'Главное меню', 'Ana Menü', 'القائمة الرئيسية', main_menu.id])

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

# Create menu items and update translations with raw SQL
created_count = 0
with connection.cursor() as cursor:
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
        
        # Update translation fields using raw SQL (modeltranslation has issues with direct assignment)
        cursor.execute("""
            UPDATE core_menuitem 
            SET title_en = %s, title_ru = %s, title_tr = %s, title_ar = %s
            WHERE id = %s
        """, [item_data['title_en'], item_data['title_ru'], item_data['title_tr'], item_data['title_ar'], item.id])
        
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

# Verification
print("\n📋 Verification:")
items = MenuItem.objects.all().order_by('order')
for item in items:
    print(f"  {item.order}. EN: {item.title_en} | RU: {item.title_ru} | TR: {item.title_tr} | AR: {item.title_ar}")
print("=" * 80)
