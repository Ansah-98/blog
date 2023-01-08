from django.contrib import admin
from .models import Post 
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display =  ('title' ,'slug' , 'author','publish', 'status')
    list_filter = ('status', 'created' , 'publish', 'author')
    prepopulated_fields ={'slug':['title']}
    search_fields = ('title','author')
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ('status','publish')
