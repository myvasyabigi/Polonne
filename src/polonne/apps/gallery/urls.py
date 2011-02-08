#-*- coding:utf-8 -*-

from django.conf.urls.defaults import *
from django.core.urlresolvers import reverse

urlpatterns = patterns(
    'gallery.views',
    url(r'^$', 'album_list', name="gallery"),


)

