import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vaam_project.settings')
import django
django.setup()

from django.utils import translation
from django.utils.translation import gettext as _
from core.models import Menu, MenuItem

# Test translations
for lang in ['en', 'tr', 'ru', 'ar']:
    translation.activate(lang)
    print(f"[{lang}] trans('Our Works') = {repr(_('Our Works'))}")

# Test DB menu
translation.activate('en')
menus = Menu.objects.filter(is_active=True).prefetch_related('items', 'items__children')
print(f"\nMenus found: {menus.count()}")
for menu in menus:
    print(f"  Menu: {menu.title!r} location={menu.location!r} is_active={menu.is_active}")
    items = menu.items.filter(parent__isnull=True, is_active=True)
    print(f"  Root items: {items.count()}")
    for item in items:
        print(f"    [{item.id}] title={item.title!r} title_en={item.title_en!r} title_tr={getattr(item,'title_tr',None)!r}")

# Test for TR
print("\n== TR language ==")
translation.activate('tr')
for menu in menus:
    items = menu.items.filter(parent__isnull=True, is_active=True)
    for item in items:
        print(f"  [{item.id}] title (TR)={item.title!r}")
