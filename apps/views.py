from django.shortcuts import render

from apps.models import Product, Category, Member


def index_view(request):
    search = request.GET.get('search')
    if search:
        products = Product.objects.filter(category__name__icontains=search)
    else:
        products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, 'apps/index.html', context)


def main_view(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'apps/main.html', context)


def member_view(request):
    members = Member.objects.all()
    context = {
        'members': members
    }
    return render(request, 'apps/member.html', context)
