"""Template tags for multilingual form field handling in dashboard."""
from django import template
from django.conf import settings

register = template.Library()

LANG_CODES = [code for code, name in settings.LANGUAGES]
LANG_NAMES = {code: name for code, name in settings.LANGUAGES}
LANG_SUFFIXES = tuple(f'_{code}' for code in LANG_CODES)
LANG_FLAGS = {
    'en': 'gb',
    'ru': 'ru',
    'tr': 'tr',
    'ar': 'sa',
}


@register.filter
def is_translation_field(field_name):
    """Check if a field name ends with a language suffix."""
    return any(field_name.endswith(f'_{code}') for code in LANG_CODES)


@register.filter
def field_lang(field_name):
    """Return the language code of a translation field."""
    for code in LANG_CODES:
        if field_name.endswith(f'_{code}'):
            return code
    return ''


@register.filter
def field_base_name(field_name):
    """Strip language suffix from a translation field name."""
    for code in LANG_CODES:
        suffix = f'_{code}'
        if field_name.endswith(suffix):
            return field_name[:-len(suffix)]
    return field_name


@register.simple_tag
def get_languages():
    """Return list of (code, name, flag_country_code) tuples."""
    return [(code, name, LANG_FLAGS.get(code, code)) for code, name in settings.LANGUAGES]


@register.filter
def lang_name(code):
    """Return language name for a code."""
    return LANG_NAMES.get(code, code)


@register.filter
def lang_flag(code):
    """Return flag country code for flagcdn.com."""
    return LANG_FLAGS.get(code, code)


@register.filter
def is_wide_field(field):
    """Check if a field should span full width (textarea, long text etc)."""
    name = field.name
    base = field_base_name(name)
    wide_bases = [
        'description', 'content', 'message', 'features', 'google_maps_embed',
        'bio', 'history', 'mission', 'vision', 'values', 'answer', 'admin_notes',
        'summary', 'short_description', 'site_description', 'meta_description',
        'meta_keywords', 'question',
    ]
    from django.forms import Textarea
    if isinstance(field.field.widget, Textarea):
        return True
    return base in wide_bases
