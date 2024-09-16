from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Product

def show_main(request):
    products = Product.objects.all()

    context = {
        'name' : 'Pan-Pan Self Portrait',
        'price': 'Rp. 200.000',
        'stock': '10',
        'description': 'A self portrait of Pan-Pan, the panda.',
        'products': products
    }

    return render(request, "main.html", context)

def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:show_main")

    context = {'form': form}
    return render(request, "add_product.html", context)