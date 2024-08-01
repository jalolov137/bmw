

from typing import Optional
from online_market.models import Product, Category, Comment
# Create your views here.
from django.shortcuts import render, get_object_or_404, render, redirect
from .forms import OrderForm
from django.http import HttpResponse

def product_list(request, category_id: Optional[int] = None):
    categories = Category.objects.all().order_by('id')
    if category_id:

        products = Product.objects.filter(category=category_id)

    else:
        products = Product.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'online_market/home.html', context)


def product_detail(request, product_id):
    comments = Comment.objects.all()
    try:
        product = get_object_or_404(Product, id=product_id)
        return render(request, 'online_market/detail.html', {'product': product, 'comments': comments})
    except:
        return HttpResponse('product not found', status=404)

def categories(request):
    category_list = Category.objects.all()
    context = {
        'categories': category_list
    }
    return render(request, 'online_market/home.html', context)

def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_success')
        else:
            form = OrderForm()
            return render(request, 'online_market/home.html', {'form': form})