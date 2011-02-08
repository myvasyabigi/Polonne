from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from models import Seo
from models import Tags
from models import Category
from models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display=('__unicode__', 'is_published',)
    list_filter=('is_published',)
    search_fields = ('content', 'title',)

class SeoAdmin(admin.ModelAdmin):
    pass
    
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title_ua",)}
    list_display = ('__unicode__', 'thumb', 'slug', 'created', 'updated')
    search_fields = ('slug', 'title')
    list_filter = ('created', 'updated')
    


admin.site.register(Seo, SeoAdmin)

admin.site.register(Tags)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)