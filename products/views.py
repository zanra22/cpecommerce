from django.shortcuts import render
from .models import Product
# Create your views here.
from django.views.generic import ListView, DetailView


class ProductListView(ListView):
    queryset = Product.objects.all()
    print(queryset)
    template_name = "products/list.html"


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    print(queryset)
    template_name = "products/detail.html"