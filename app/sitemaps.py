"""
Project sitemaps
"""
from django.contrib import sitemaps
from django.contrib.auth import get_user_model
from django.urls import reverse


class UserSitemap(sitemaps.Sitemap):
    """
    Return sitemap with users that have at least one public camera
    """
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return get_user_model().objects.filter(legacy=False)

    def location(self, obj):
        return obj.get_absolute_url()


class StaticSitemap(sitemaps.Sitemap):
    """Reverse 'static' views for XML sitemap."""
    changefreq = 'daily'
    priority = 1

    def items(self):
        """
        :return: Return list of url names for views to include in sitemap
        """
        return [
            'website:front',
            'website:takedown',
            'website:agreement',
            'website:contacts',
        ]

    def location(self, item):
        return reverse(item)


sitemap_config = {
    'sitemaps': {
        'static': StaticSitemap(),
        'users': UserSitemap(),
    }
}
