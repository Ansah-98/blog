from django.contrib.sitemaps import Sitemap

from .models import Post 

class PostSite(Sitemap):
    changefreq = 'weekly'
    priority  = 0.9

    def items(self):
        Post.objects.all()
    
    def lastmod(self,obj):
        return obj.updated