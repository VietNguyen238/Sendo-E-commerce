from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
import json


def format_vnd(price):
    # Ensure price is numeric
    try:
        price = float(price)
    except (TypeError, ValueError):
        return price

    # Format the price as VND
    formatted_price = "{:,.0f}".format(price)
    return formatted_price


def paymentSuccess(request):
    return render(request, "paymentSuccess.html")


def register(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    return render(request, "register.html", {"form": form})


def index(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, create = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_quantity
        for i in range(0, len(items)):
            items[i].product.new_price = format_vnd(items[i].product.new_price)
            items[i].product.old_price = format_vnd(items[i].product.old_price)
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_quantity": 0, "address": False}
        cartItems = order["get_cart_quantity"]

    products = Product.objects.all().order_by("-date")
    for product in products:
        product.new_price = format_vnd(product.new_price)
        product.old_price = format_vnd(product.old_price)
    Data = {"Products": products, "cartItems": cartItems}

    return render(request, "store.html", Data)


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, create = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_quantity
        for i in range(0, len(items)):
            items[i].product.new_price = format_vnd(items[i].product.new_price)
            items[i].product.old_price = format_vnd(items[i].product.old_price)

    else:
        cartItems = order["get_cart_quantity"]
        items = []
        order = {"get_cart_total": 0, "get_cart_quantity": 0, "address": False}

    context = {"items": items, "order": order, "cartItems": cartItems}
    return render(request, "cart.html", context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, create = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_quantity
        for i in range(0, len(items)):
            items[i].product.new_price = format_vnd(items[i].product.new_price)
            items[i].product.old_price = format_vnd(items[i].product.old_price)

    else:
        cartItems = order["get_cart_quantity"]
        items = []
        order = {"get_cart_total": 0, "get_cart_quantity": 0, "address": False}

    context = {"items": items, "order": order, "cartItems": cartItems}
    return render(request, "checkout.html", context)


def product(request, id):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, create = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_quantity
        for i in range(0, len(items)):
            items[i].product.new_price = format_vnd(items[i].product.new_price)
            items[i].product.old_price = format_vnd(items[i].product.old_price)
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_quantity": 0, "address": False}
        cartItems = order["get_cart_quantity"]

    product = Product.objects.get(id=id)
    product.new_price = format_vnd(product.new_price)
    product.old_price = format_vnd(product.old_price)
    data = {
        "product": product,
        "items": items,
        "cartItems": cartItems,
    }
    return render(request, "product.html", data)


def updateItem(request):
    data = json.loads(request.body)
    productId = data["productId"]
    action = data["action"]

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, completed=False)
    items = order.orderitem_set.all()
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    purchase, created = Purchase.objects.get_or_create()
    for i in range(0, len(items)):
        items[i].product.quantity = product.quantity
        quantityProduct = items[i].product.quantity

    if action == "addAQuantity":
        if purchase.purchase < quantityProduct:
            purchase.purchase = purchase.purchase + 1
        else:
            purchase.purchase = quantityProduct
    elif action == "removeAQuantity":
        if purchase.purchase > 1:
            purchase.purchase = purchase.purchase - 1
        else:
            orderItem.purchase = 1
    if action == "addQuantity":
        if orderItem.quantity < quantityProduct:
            orderItem.quantity = orderItem.quantity + purchase.purchase
        purchase.purchase = 1
    purchase.save()
    if action == "add":
        if orderItem.quantity < quantityProduct:
            orderItem.quantity = orderItem.quantity + 1
        else:
            orderItem.quantity = quantityProduct
    elif action == "remove":
        if orderItem.quantity > 1:
            orderItem.quantity = orderItem.quantity - 1
        else:
            orderItem.quantity = 1
    elif action == "delete":
        orderItem.quantity = orderItem.quantity - orderItem.quantity

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse("Item was added", safe=False)


def address(request):
    return render(request, "address.html")
