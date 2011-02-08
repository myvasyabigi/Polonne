from django.contrib import admin

from models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'pub_date', 'is_published',]
    
admin.site.register(News, NewsAdmin)
