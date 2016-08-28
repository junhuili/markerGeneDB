# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from models import Taxon, Valid, Typestrain

admin.site.register(Taxon)
admin.site.register(Valid)
admin.site.register(Typestrain)

