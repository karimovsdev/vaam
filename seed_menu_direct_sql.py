"""
VAAM - Direct SQL Update for Menu Item Translations
Run: python seed_menu_direct_sql.py
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vaam_project.settings')
django.setup()

from django.db import connection
from core.models import MenuItem

print("=" * 80)
print("  VAAM - Updating Menu Item Translations via Direct SQL")
print("=" * 80)

# Menu translations data
menu_translations = [
    {'en': 'Home', 'ru': 'Главная', 'tr': 'Ana Sayfa', 'ar': 'الرئيسية', 'order': 1},
    {'en': 'About Us', 'ru': 'О нас', 'tr': 'Hakkımızda', 'ar': 'من نحن', 'order': 2},
    {'en': 'Services', 'ru': 'Услуги', 'tr': 'Hizmetler', 'ar': 'الخدمات', 'order': 3},
    {'en': 'Products', 'ru': 'Продукция', 'tr': 'Ürünler', 'ar': 'المنتجات', 'order': 4},
    {'en': 'Projects', 'ru': 'Проекты', 'tr': 'Projeler', 'ar': 'المشاريع', 'order': 5},
    {'en': 'News', 'ru': 'Новости', 'tr': 'Haberler', 'ar': 'الأخبار', 'order': 6},
    {'en': 'Contact', 'ru': 'Контакт', 'tr': 'İletişim', 'ar': 'اتصل بنا', 'order': 7},
]

# Update using raw SQL
with connection.cursor() as cursor:
    for trans in menu_translations:
        cursor.execute("""
            UPDATE core_menuitem 
            SET title_ru = %s, title_tr = %s, title_ar = %s
            WHERE "order" = %s
        """, [trans['ru'], trans['tr'], trans['ar'], trans['order']])
        print(f"  ✓ Updated: {trans['en']} → RU: {trans['ru']}, TR: {trans['tr']}, AR: {trans['ar']}")

print("\n" + "=" * 80)
print("  ✓ SUCCESS! All menu item translations updated")
print("=" * 80)

# Verify
print("\nVerification:")
items = MenuItem.objects.all().order_by('order')
for item in items:
    print(f"  {item.title_en} → RU: {item.title_ru}, TR: {item.title_tr}, AR: {item.title_ar}")

print("=" * 80)
