from django.shortcuts import render, redirect
from django.urls import reverse

from apps.models import Product, Category


def index_view(request):
    category = request.GET.get('category')
    if category:
        products = Product.objects.filter(category__slug=category)
    else:
        products = Product.objects.all()
    context = {
        "products": products,
        "categories": Category.objects.all(),
    }
    return render(request, 'apps/index.html', context)


def create_view(request):
    if request.method == 'GET':
        return render(request, 'apps/create.html')

    name = request.POST.get('name')
    price = request.POST.get('price')
    category = request.POST.get('category')
    Product.objects.create(name=name, price=price, category_id=category)
    return redirect(reverse('index'))
