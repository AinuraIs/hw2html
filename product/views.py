from django.shortcuts import render, redirect, get_object_or_404

from product.form import ProductForm
from product.models import Product


def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context = {'product': products}
        return render(request, 'product/products.html', context=context)
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products/')


def product_detail(request, pk):
    if request.method == 'GET':
        product = Product.objects.get(pk=pk)
        context = {'product': product}
        return render(request, 'product/product_detail.html', context=context)
    if request.method == 'PUT':
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products/', pk=product.pk)
    if request.method == 'DELETE':
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return redirect('products/')
