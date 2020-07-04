from math import ceil
from django.views.generic import ListView
from django.utils import timezone
from django.urls import reverse
from django.shortcuts import render, redirect
from . import models


class HomeView(ListView):
    """ HomeView Definition """

    model = models.Product
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context


def product_detail(request, pk):
    try:
        page = request.GET.get("page", 1)
        page = int(page or 1)
        page_size = 2
        page_offset = page_size * page - page_size

        product = models.Product.objects.get(pk=pk)

        page_count = ceil(product.projects.count() / page_size)
        projects = product.projects.all()[page_offset : page_offset + page_size]

        return render(
            request,
            "products/detail.html",
            {
                "product": product,
                "projects": projects,
                "page": page,
                "page_count": page_count,
            },
        )
    except models.Product.DoesNotExist:
        return redirect(reverse("core:home"))


def search(request):
    product = request.GET.get("product_name", "product")
    return render(request, "products/search.html", {"product": product})
