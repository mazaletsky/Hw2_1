from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    print(request.GET)
    sort=request.GET.get('sort')
    query_set=Phone.objects.all()
    if sort:
        if sort=='name':
            query_set=Phone.objects.all().order_by('name')
        elif sort=='min_price':
            query_set=Phone.objects.all().order_by('price')
        elif sort=='max_price':
            query_set=Phone.objects.all().order_by('-price')
    context = {'phones': query_set}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug)}
    return render(request, template, context)
