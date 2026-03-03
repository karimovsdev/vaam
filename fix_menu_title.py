import os, sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vaam_project.settings')
import django
django.setup()

from core.models import MenuItem

items = MenuItem.objects.all()
print("All MenuItems:")
for i in items:
    print(f"  id={i.id}  title={i.title!r}  title_en={getattr(i,'title_en',None)!r}  title_tr={getattr(i,'title_tr',None)!r}  title_ru={getattr(i,'title_ru',None)!r}  title_ar={getattr(i,'title_ar',None)!r}")

# Update Projects -> Our Works
updated = 0
for item in items:
    changed = False
    if getattr(item, 'title_en', None) == 'Projects':
        item.title_en = 'Our Works'
        changed = True
    if getattr(item, 'title_tr', None) in ('Projects', 'Projeler'):
        item.title_tr = 'İşlerimiz'
        changed = True
    if getattr(item, 'title_ru', None) in ('Projects', 'Проекты'):
        item.title_ru = 'Наши работы'
        changed = True
    if getattr(item, 'title_ar', None) in ('Projects', 'المشاريع'):
        item.title_ar = 'أعمالنا'
        changed = True
    if changed:
        item.save()
        updated += 1
        print(f"Updated id={item.id}: EN={item.title_en!r} TR={getattr(item,'title_tr',None)!r} RU={getattr(item,'title_ru',None)!r} AR={getattr(item,'title_ar',None)!r}")

print(f"Done. {updated} item(s) updated.")
