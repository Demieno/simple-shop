from django.shortcuts import render
from decimal import Decimal
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import *

def index(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id = cart_id)
        request.session['total'] = cart.products.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        cart_id = request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id = cart_id)
   
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories':categories,
        'products':products,
        'cart':cart
    }
    return render(request,'base.html',context)

def product(request, product_slug):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id = cart_id)
        request.session['total'] = cart.products.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        cart_id = request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id = cart_id)
    
    product = Product.objects.get(slug = product_slug) 
    context = {
        'cart':cart,
        'product':product
    }
    return render(request,'product.html',context)

def category(request, category_slug):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id = cart_id)
        request.session['total'] = cart.products.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        cart_id = request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id = cart_id)
    category = Category.objects.get(slug = category_slug)
    context = {
        'cart':cart,
        'category':category
    }
    return render(request,'category.html',context)

def cart(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id = cart_id)
        request.session['total'] = cart.products.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        cart_id = request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id = cart_id)
    cart_items = CartItem.objects.all()
    for item in cart_items:
        cart.total +=item.total
    form = PromocodeForm

    if request.method == "POST":
        code = request.POST.get("code")
        promocode = PromoCode.objects.filter(title = code)
    else:
        promocode = PromoCode.objects.filter(title = 'Null')
    for code in promocode:
        cart.total-= code.total
    cart.save 
    context = {
        'form': form,
        'cart': cart,
        'promocode':promocode
    }
    return render(request,'cart.html',context)

def add_to_cart(self,product_slug):
    product = Product.objects.get(slug=product_slug)
    item,_ = CartItem.objects.get_or_create(product = product,total = product.cost)
    cart  = Cart.objects.first()
    if item not in cart.products.all():
        cart.products.add(item)
        item.quantity = 1 
        item.save()
        cart.save()
        return HttpResponseRedirect('/')

def increase_item(self,product_slug):
    product = Product.objects.get(slug=product_slug)
    cart  = Cart.objects.first()
    item = cart.products.get(product = product)
    item.quantity += 1
    item.save()
    return HttpResponseRedirect('/cart/')

def remove_from_cart(self,product_slug):
    product = Product.objects.get(slug=product_slug)
    cart  = Cart.objects.first()
    item = cart.products.get(product = product)
    item.delete()
    cart.save()
    return HttpResponseRedirect('/cart/')

def decrease_item(self,product_slug):
    product = Product.objects.get(slug=product_slug)
    cart  = Cart.objects.first()
    item = cart.products.get(product = product)
    item.quantity -= 1
    cart.total -= item.total
    if cart.total < 0:
        cart.total = 0
    if item.quantity <1:
        item.delete()
    item.save()
    cart.save()
    return HttpResponseRedirect('/cart/')




##
def login(request):
    test = Test.objects.all()
    context = {'test': test}
    return render(request,'login.html',context)

def logout(request):
    test = Test.objects.all()
    context = {'test': test}
    return render(request,'base.html',context)

def registration(request):
    test = Test.objects.all()
    context = {'test': test}
    return render(request,'base.html',context)


