"""
SEO template tags for multilingual hreflang URL generation.
"""
from django import template
from django.conf import settings

register = template.Library()

LANG_CODES = [code for code, _ in settings.LANGUAGES]


@register.simple_tag(takes_context=True)
def alternate_url(context, lang_code):
    """
    Return the absolute URL of the current page translated to the given language.

    URL structure (i18n_patterns with prefix_default_language=True):
        /en/products/slug/
        /ru/products/slug/
    So we just replace the first path segment with the target lang_code.
    """
    request = context.get('request')
    if not request:
        return ''
    path = request.path  # e.g. /en/products/slug/
    # Split into at most 3 parts: ['', 'en', 'products/slug/']
    parts = path.split('/', 2)
    if len(parts) >= 2 and parts[1] in LANG_CODES:
        parts[1] = lang_code
        new_path = '/'.join(parts)
    else:
        new_path = f'/{lang_code}/{path.lstrip("/")}'
    return f'{request.scheme}://{request.get_host()}{new_path}'
