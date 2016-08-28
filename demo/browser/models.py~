# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
import datetime

@python_2_unicode_compatible
class Taxon(models.Model):
    RANK_CHOICES = [(1,"Kingdom"), (2,"Phylum"), (3,"Class"), (4,"Order"), (5,"Family"), (6,"Genus"), (7,"Species")]

    name = models.CharField(_("Name"), max_length=255)
    rank = models.SmallIntegerField(choices=RANK_CHOICES)
    last_update = models.DateField(_("Date"), default=datetime.date.today)
    class Meta:
        verbose_name_plural = "taxa"
  
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
    seq_id = models.IntegerField(_("Sequence ID Number"))
    category_abbrv = models.CharField(_("Category Abbreviation"), max_length=100)

    def __unicode__(self):
        return unicode(self.taxon)

    def __str__(self):
        return str(self.taxon)


@python_2_unicode_compatible
class Valid(models.Model):
    taxon = models.OneToOneField(
        Taxon,
        on_delete=models.CASCADE,
        primary_key=True,
    )

#    rank = models.CharField(_("ATCC Number"), max_length=20)
    category_abbrv = models.CharField(_("Category Abbreviation"), max_length=100)
    seq_id = models.IntegerField(_("Sequence ID Number"))

    class Meta:
        verbose_name_plural = "valid names"

    def __str__(self):
        return str(self.taxon)

    def __unicode__(self):
        return unicode(self.taxon)

@python_2_unicode_compatible
class Invalid(models.Model):
    taxon = models.OneToOneField(
        Taxon,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    reference_url = models.URLField("(blank=True, default='')")

    class Meta:
        verbose_name_plural = "invalid names"

    def __str__(self):
        return str(self.taxon)

    def __unicode__(self):
        return unicode(self.taxon)


@python_2_unicode_compatible
class Synonym(models.Model):
    taxon = models.OneToOneField(
        Taxon,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    valid_name = models.ForeignKey(Valid, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.taxon)

    def __unicode__(self):
        return unicode(self.taxon)


@python_2_unicode_compatible
class Candidatus(models.Model):
    taxon = models.OneToOneField(
        Taxon,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    seq_id = models.IntegerField(_("Sequence ID Number"))

    class Meta:
        verbose_name_plural = "candidates"


    def __str__(self):
        return str(self.taxon)

    def __unicode__(self):
        return unicode(self.taxon)

@python_2_unicode_compatible
class Reference(models.Model):
    taxon = models.OneToOneField(
        Taxon,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    authors = models.CharField(_("Author List"), max_length=100)
    journal = models.CharField(_("Journal Title"), max_length=100)
    publication_date = models.CharField(_("Journal Publication Date"), max_length=100)

    def __str__(self):
        return str(self.taxon)

    def __unicode__(self):
        return unicode(self.taxon)


@python_2_unicode_compatible
class Sequence(models.Model):
    taxon = models.OneToOneField(
        Taxon,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    nuc_sequence = models.TextField(_("Nucleotide Sequence"))
    seq_id = models.IntegerField(_("Sequence ID Number"))

    def __str__(self):
        return str(self.taxon)

    def __unicode__(self):
        return unicode(self.taxon)



