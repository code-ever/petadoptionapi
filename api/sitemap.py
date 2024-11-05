from django.contrib.sitemaps import Sitemap
from .models import Uploadpets

class UploadSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9
    def items(self):
        return Uploadpets.objects.all()

    def lastmod(self,obj):
        return obj.uploade_date
    
   