# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.conf.urls import patterns, url

#from .views import taxon_list
from .views import TaxonListView


urlpatterns = patterns('',
    url(r'^$', 'browser.views.taxon_list', name="taxon_list"),
    url(r'^alternative/$', TaxonListView.as_view(), name="taxon_list"),
)


from django.conf.urls import url

from . import views


