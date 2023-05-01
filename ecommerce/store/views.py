import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import *


# Create your views here.
def store(request):


    if request.user.is_authenticated:
        customer = request.user.customer
        # getting the customer order
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render(request, 'store/store.html', context)

    

def cart(request):
    # setting the conditions for an authenticated user and a non-authenticated user
    if request.user.is_authenticated:
        customer = request.user.customer
        # getting the customer order
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items'] 

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'store/cart.html', context)

def checkout(request):
     # setting the conditions for an authenticated user and a non-authenticated user
    if request.user.is_authenticated:
        customer = request.user.customer
        # getting the customer order
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
        
    context = {'items':items, 'order':order, 'cartItems':cartItems}
   
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data[productId]
    action = data['action']
    print('Action:', action)
    print('productId:', productId)
    

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderitem, created = orderitem.get_or_create(order=order, product=product)

    if action == 'add':
        orderitem.quantity = ( orderitem.quantity + 1)
    elif action == 'remove':
        orderitem.quantity = ( orderitem.quantity - 1)
    orderitem.save()
    if orderitem <= 0:
        orderitem.delete()


