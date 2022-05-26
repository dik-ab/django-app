
from django.contrib import admin
from . import settings
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

sitemaps = {
        'static' : StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('certifications.urls')),
    path('sitemap.xml/', sitemap, {'sitemaps':sitemaps},name='django.contrib.sitemaps.views.sitemaps'),
]
