# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

RANK_CHOICES = (
    (1, "Kingdom"),
    (2, "Phylum"),
    (3, "Class"),
    (4, "Order"),
    (5, "Family"),
    (5, "Genus"),
    (5, "Species"),
)

CATEGORY_CHOICES = ["Type Strain","Valid", "Invalid", "Candidatus"]

#@python_2_unicode_compatible
#class Category(models.Model):
#    name = models.CharField(choices=CATEGORY_CHOICES)
#
#    def __str__(self):
#        return self.name

@python_2_unicode_compatible
class Taxon(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    rank = models.CharField(choices=RANK_CHOICES, max_length=15)
#    category = models.CharField(choices=CATEGORY_CHOICES)
 #   category = models.ForeignKey(Category, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Typestrain(models.Model):

    taxon = models.OneToOneField(
        Taxon,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    atcc_num = models.CharField(_("ATCC Number"), max_length=15)
    dsm_num = models.CharField(_("DSM Number"), max_length=15)
    seq_id = models.CharField(_("Sequence ID Number"), max_length=100)
    category_abbrv = models.CharField(_("Category Abbreviation"), max_length=100)
    def __str__(self):
        return self.taxon


@python_2_unicode_compatible
class Valid(models.Model):

    taxon = models.OneToOneField(
        Taxon,
        on_delete=models.CASCADE,
        primary_key=True,
    )
#    name = models.CharField(_("Correct Name"), max_length=100)
    rank = models.CharField(_("ATCC Number"), max_length=20)
    category_abbrv = models.CharField(_("Category Abbreviation"), max_length=100)
    seq_id = models.CharField(_("Sequence ID Number"), max_length=100)

    def __str__(self):
        return self.name





