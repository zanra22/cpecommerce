from django.shortcuts import render, redirect

from products.models import Product
from .models import Cart
# Create your views here.

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    # cart_id = request.session.get('cart_id', None)
    # if cart_id is None:
    #     request.session['cart_id'] = 1
    # else:
    #     print("exist")
    return render(request, "carts/home.html", {})


def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return redirect('cart:cart_home')
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
    return redirect('cart:cart_home')