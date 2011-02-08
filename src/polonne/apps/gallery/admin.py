from django.contrib import admin

from models import Album
from models import Photo

class AlbumAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'thumb']

admin.site.register(Album, AlbumAdmin)

class PhotoAdmin(admin.ModelAdmin):
    list_display=['__unicode__', 'thumb']

admin.site.register(Photo, PhotoAdmin)