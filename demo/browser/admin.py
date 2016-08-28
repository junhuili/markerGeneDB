# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from models import Taxon, Valid, Typestrain, Invalid, Synonym, Candidatus, Reference, Sequence

admin.site.register(Taxon)
admin.site.register(Valid)
admin.site.register(Invalid)
admin.site.register(Typestrain)
admin.site.register(Synonym)
admin.site.register(Candidatus)
admin.site.register(Reference)
admin.site.register(Sequence)

