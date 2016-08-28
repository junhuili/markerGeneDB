# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import View


from .models import Typestrain, Valid, Taxon
from .forms import TaxonFilterForm


def taxon_list(request):
    paginate_by = 15
    qs = Taxon.objects.order_by("name")
    
    form = TaxonFilterForm(data=request.GET)

    facets = {
        "selected": {},
        "categories": {
            "typestrain": Typestrain.objects.all(),
            "valid": Valid.objects.all(),
        },
    }

    if form.is_valid():
        typestrain = form.cleaned_data["typestrain"]
        if typestrain:
            facets["selected"]["typestrain"] = typestrain
            qs = qs.filter(typestrain=typestrain).distinct()

        valid = form.cleaned_data["valid"]
        if valid:
            facets["selected"]["valid"] = valid
            qs = qs.filter(valid=valid).distinct()

#        if rating:
#            rating = int(rating)
#            facets["selected"]["rating"] = (rating, dict(RATING_CHOICES)[rating])
#            qs = qs.filter(rating=rating).distinct()

    paginator = Paginator(qs, paginate_by)

    page_number = request.GET.get("page")
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, show first page.
        page = paginator.page(1)
    except EmptyPage:
        # If page is out of range, show last existing page.
        page = paginator.page(paginator.num_pages)

    context = {
        "form": form,
        "facets": facets,
        "object_list": page,
    }
    return render(request, "taxa/taxon_list.html", context)


class TaxonListView(View):
    form_class = TaxonFilterForm
    template_name = "browser/taxa_list.html"
    paginate_by = 15

    def get(self, request, *args, **kwargs):
        form = self.form_class(data=request.GET)
        qs, facets = self.get_queryset_and_facets(form)
        page = self.get_page(request, qs)
        context = {
            "form": form,
            "facets": facets,
            "object_list": page,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def get_queryset_and_facets(self, form):
        qs = Taxon.objects.order_by("name")

        facets = {
            "selected": {},
            "categories": {
                "typestrains": Typestrain.objects.all(),
                "valid": Valid.objects.all(),
            },
        }
        if form.is_valid():
            typestrain = form.cleaned_data["typestrain"]
            if typestrain:
                facets["selected"]["typestrain"] = typestrain
                qs = qs.filter(typestrains=typestrain).distinct()

            taxon = form.cleaned_data["taxon"]
            if taxon:
                facets["selected"]["taxon"] = taxon
                qs = qs.filter(taxa=taxon).distinct()

        return qs, facets

    def get_page(self, request, qs):
        paginator = Paginator(qs, self.paginate_by)

        page_number = request.GET.get("page")
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            # If page is not an integer, show first page.
            page = paginator.page(1)
        except EmptyPage:
            # If page is out of range, show last existing page.
            page = paginator.page(paginator.num_pages)
        return page
