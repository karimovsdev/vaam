from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        from django.db.models.signals import post_save, post_delete
        from django.core.cache import cache

        def clear_context_cache(sender, **kwargs):
            """Clear context_processor cache when relevant models change."""
            # Delete all language variants of the cache
            for lang in ('en', 'ru', 'az', 'ar'):
                cache.delete(f'ctx_site_settings_{lang}')

        from .models import SiteSettings, Service, Menu, MenuItem, Page
        for model in (SiteSettings, Service, Menu, MenuItem, Page):
            post_save.connect(clear_context_cache, sender=model)
            post_delete.connect(clear_context_cache, sender=model)
