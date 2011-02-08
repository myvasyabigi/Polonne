#-*- coding:utf-8 -*-

from django.db import models
from django.db.models import permalink
from django.template import Template, Context
from django.utils.translation import ugettext_lazy as _


from django_extensions.db.fields import AutoSlugField
from transmeta import TransMeta

class Album(models.Model):
    __metaclass__=TransMeta
    
    title = models.CharField(verbose_name=_("Album title"), max_length=255,
    blank=True, null=True)
    pub_date = models.DateField(auto_now_add=True) 
    change_date = models.DateField(auto_now = True)
    slug = AutoSlugField(populate_from=lambda instance: instance.title)
    description = models.TextField(verbose_name = _("Description"),
        blank=True, null=True)
    album_image = models.ImageField(upload_to = "albums/covers",
        verbose_name=_("Is main photo"), blank=True, null=True)
    
    class Meta:
        verbose_name = ("Album")
        verbose_name_plural = ("Albums")
        ordering = ['-pub_date', '-change_date']
        translate = ('title', 'description')
    
    def __unicode__(self):
        return self.title
        
    def album_photos_count(self):
        count = self.photo_set.all().count()
        return count
        
    def thumb(self):
        t = Template("""
        {% load thumbnail %}
        <a href="#"> <img src="{% thumbnail image.album_image 127x127  crop  %}"/> </a>
        """)
        c = Context({"image":self})
        thum = t.render(c)
        
        return  thum
    thumb.short_description = 'Album image'
    thumb.allow_tags = True
    
        

class Photo(models.Model):
    __metaclass__ = TransMeta
    title = models.CharField(verbose_name = _("title"), blank=True,
        null=True, max_length=255)
    album = models.ForeignKey(Album, verbose_name = _("Choose or create album"), 
        blank=True, null=True)
    pub_date = models.DateField(auto_now_add=True) 
    change_date = models.DateField(auto_now = True)
    image = models.ImageField(upload_to="albums/photos",
        verbose_name = _("Choose a photo"))
    source = models.CharField(_("Source"), max_length=255,
        blank=True, null=True)

    class Meta:
        verbose_name = _("Photo")
        verbose_name_plural = _("Photos")
        ordering = ['-pub_date']
        translate = ('title',)
        
    def __unicode__(self):
        if self.title:
            return self.title
        return str(self.id)
        
    def thumb(self):
        t = Template("""
        {% load thumbnail %}
        <a href="#">{% thumbnail image.image "127x127"  crop="center" as im  %}<img src="{{ im.url }}"/>{% endthumbnail %}</a>
        """)
        c = Context({"image":self})
        thum = t.render(c)
        return  thum
    thumb.short_description = 'Image'
    thumb.allow_tags = True
    
    

