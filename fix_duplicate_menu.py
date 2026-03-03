import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vaam_project.settings')
import django
django.setup()

from core.models import Menu, MenuItem

# Show all menus with their IDs
print("=== All Menus ===")
for m in Menu.objects.all().order_by('id'):
    count = m.items.filter(parent__isnull=True, is_active=True).count()
    print(f"  id={m.id}  location={m.location!r}  title={m.title!r}  items={count}  is_active={m.is_active}")

# Delete duplicate empty 'main' menus (keep the one with items)
main_menus = list(Menu.objects.filter(location='main', is_active=True).order_by('id'))
print(f"\n'main' menus: {len(main_menus)}")

if len(main_menus) > 1:
    # Keep the one with more items
    best = max(main_menus, key=lambda m: m.items.filter(parent__isnull=True, is_active=True).count())
    to_delete = [m for m in main_menus if m.id != best.id]
    for m in to_delete:
        print(f"  Deleting empty duplicate: id={m.id}  items={m.items.count()}")
        m.delete()
    print(f"  Kept: id={best.id} with {best.items.filter(parent__isnull=True, is_active=True).count()} root items")
else:
    print("  No duplicates found.")

print("Done.")
