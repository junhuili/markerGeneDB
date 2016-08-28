# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Typestrain
from .models import Valid


class TaxonFilterForm(forms.Form):
    typestrain = forms.ModelChoiceField(
        label=_("Type Strains"),
        required=False,
        queryset=Typestrain.objects.all(),
    )
    valid = forms.ModelChoiceField(
        label=_("Valid Names"),
        required=False,
        queryset=Valid.objects.all(),
   )

