"""
URL configuration for vaam_project project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import RedirectView

# Dashboard URLs (no language prefix)
urlpatterns = [
    path('admin/', RedirectView.as_view(url='/dashboard/', permanent=True)),
    path('dashboard/', include('dashboard.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]

# Front-end URLs (with language prefix: /en/, /ru/, /tr/, /ar/)
urlpatterns += i18n_patterns(
    path('', include('core.urls')),
    prefix_default_language=True,
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
