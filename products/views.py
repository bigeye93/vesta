from django.shortcuts import render
from . import models

# from django.http import HttpResponse


def all_products(request):
    # return HttpResponse(content="hello")
    all_products = models.Product.objects.all()
    return render(request, "products/home.html", context={"products": all_products,})
