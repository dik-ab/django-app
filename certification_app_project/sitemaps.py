from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority=0.5
    changefreq='weekly'
    protocol='https'

    def items(self):
        return ['sitemap:certification_list']

    def location(self, item):
        return reverse(item)
