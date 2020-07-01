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
        product = models.Product.objects.get(pk=pk)
        return render(request, "products/detail.html", {"product": product})
    except models.Product.DoesNotExist:
        return redirect(reverse("core:home"))

