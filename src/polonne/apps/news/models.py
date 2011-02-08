#-*- coding:utf-8 -*-

from django.db import models
from django.db.models import permalink
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import AutoSlugField

from articles.models import Tags
from transmeta import TransMeta


class Category(models.Model):
    __metaclass__ = TransMeta

    parent = models.ForeignKey('self', verbose_name=_("Parent directory"),
        blank=True, null=True, related_name='children')
    title = models.CharField(_("Title"), max_length=255,
        blank=True, null=True)
    slug = models.SlugField(_("Slug"))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='category/images', 
        verbose_name=_("Category image"), blank=True, null=True)
    image_name = models.CharField(editable=False, max_length=255, 
        blank=True, null=True)
    objects = models.Manager()

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        translate = ('title',)

    def __unicode__(self):
        return self.title


class News(models.Model):
    __metaclass__ = TransMeta

    category = models.ForeignKey(Category, blank=True, null=True)
    title = models.CharField(_("Title"),
        max_length=255, blank=True, null=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    pub_date = models.DateField(auto_now_add=True, verbose_name=("Publication date")) 
    change_date = models.DateField(auto_now = True)
    content = models.TextField(verbose_name=_("Text"))
    is_published = models.BooleanField(verbose_name=_("Published"))
    source = models.CharField(_("Source"), max_length=255,
        blank=True, null=True)
    
    
    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")
        ordering = ['-pub_date']
        translate = ('title', 'content')
        
    def __unicode__(self):
        return self.title
    
