# -*- coding: utf-8 -*-
import mptt
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template import Template, Context
from django.db.models.signals import post_save
from django.core.cache import cache

from people.models import Profile

from transmeta import TransMeta

class Seo(models.Model):
    __metaclass__ = TransMeta
    
    title = models.CharField(_("Title"), max_length=255,
        help_text=_("Meta title"), blank=True, null=True)
    keywords = models.TextField(_("Keywords"), max_length=255,
        help_text=_("Meta keywords"), blank=True, null=True)
    description = models.TextField(_("Description"), max_length=255,
        help_text=_("Meta description"), blank=True, null=True)

    class Meta:
        verbose_name=_("Meta data")
        verbose_name_plural=_("Meta datas")
        translate = ('title', 'keywords', 'description')


    def __unicode__(self):
        return self.title


class Tags(models.Model):
    __metaclass__ = TransMeta
    
    title = models.CharField(_("Title"), max_length=255,
    blank=True, null=True)
    slug = models.SlugField(_("Slug"),
        help_text=_("This link will be a part of URL"))

    class Meta:
        verbose_name=_("Tag")
        verbose_name_plural=_("Tags")
        translate = ('title',)

    def __unicode__(self):
        return self.title


class CategoryManager(models.Manager):
    def get_top():
        super(CategoryManager, self).get_query_set()


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
    top = CategoryManager()

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        translate = ('title',)

    def __unicode__(self):
        return self.title
        
    def thumb(self):
        t = Template("""
            {% load thumbnail %}
            {% thumbnail image.image "100x100" crop="center" as im %}
            <img src="{{ im.url }}"/>{% endthumbnail %}""")
        c = Context({"image":self})
        thum = t.render(c)
        return  thum
    thumb.short_description = "Image"
    thumb.allow_tags = True

mptt.register(Category)

class Article(models.Model):
    __metaclass__ = TransMeta

    profile = models.ForeignKey(Profile, blank=True, null=True,
        verbose_name=_("Profile"))
    title = models.CharField(_("Title"), max_length=255,
        blank=True, null=True)
    slug = models.SlugField(_("Slug"))
    meta = models.ForeignKey(Seo, verbose_name=_("Meta"),
        blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name=_("Category"))
    content = models.TextField(_("Content"), blank=True, null=True)
    tags = models.ManyToManyField(Tags, verbose_name=_("Tags"),
        blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField()
    is_published = models.BooleanField()
    image_top = models.ImageField(upload_to="articles/images",
        blank=True, null=True)
    source = models.CharField(_("Source"), max_length=255,
        blank=True, null=True)

    objects = models.Manager()
    #similar = SimilarManager()

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
        translate = ('title', 'content')

    def __unicode__(self):
        return self.title

    def get_similar(self):
        slug = self.slug
        similar = Article.objects.filter(slug__contains=slug)
        return similar 
        
        
def clear_cache(sender, **kwargs):
    cache.delete('articles')
    cache.delete('categories')
    
post_save.connect(clear_cache, sender=Category, dispatch_uid="articles.clear.cache")
