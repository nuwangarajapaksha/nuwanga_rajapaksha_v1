from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        # List all your page URL names
        return ['portfolio', 'programming', 'photography', 'sports']

    def location(self, item):
        return reverse(item)
