from django import template
from ..models import Post 

register   =  template.Library()

@register.simple_tag
def total_post():
    return Post.objects.count()

@register.inclusion_tag
def latest_post(count  = 3 ):
    latest = Post.objects.order_by('-publish')[:count]
    return  {'latest': latest}