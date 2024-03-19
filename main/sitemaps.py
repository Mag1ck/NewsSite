from django.contrib.sitemaps import Sitemap
from api.models import Article

class MySitemap(Sitemap):
    changefreq = 'always'
    priority = 0.9
    def items(self):
        # Zwróć listę adresów URL do dodania do sitemapy
        return Article.objects.filter()
