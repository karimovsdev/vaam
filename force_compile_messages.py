#!/usr/bin/env python3
"""Force recompile all .po files using msgfmt directly, bypassing Django's timestamp check."""
import subprocess, os

locales = ['tr', 'ru', 'ar', 'en']
base = '/home/vaam/app/locale'

for lang in locales:
    po = f'{base}/{lang}/LC_MESSAGES/django.po'
    mo = f'{base}/{lang}/LC_MESSAGES/django.mo'
    if not os.path.exists(po):
        print(f'[skip] {lang}: no .po file')
        continue
    result = subprocess.run(['msgfmt', '-o', mo, po], capture_output=True, text=True)
    if result.returncode == 0:
        print(f'[ok]   {lang}: compiled {mo}')
    else:
        print(f'[err]  {lang}: {result.stderr}')

# Verify TR
import gettext
for lang in ['tr', 'ru', 'ar']:
    try:
        t = gettext.translation('django', localedir=base, languages=[lang])
        result = t.gettext('Our Works')
        print(f'[check] {lang} "Our Works" -> {result!r}')
    except Exception as e:
        print(f'[check] {lang} error: {e}')
