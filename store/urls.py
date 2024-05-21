from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="store"),
    path("gio-hang/", views.cart, name="cart"),
    path("product/<int:id>", views.product, name="product"),
    path("checkout/", views.checkout, name="checkout"),
    path("update_item/", views.updateItem, name="update_item"),
    path("address/", views.address, name="address"),
    path("register/", views.register, name="register"),
    path("paymentSuccess/", views.paymentSuccess, name="paymentSuccess"),
]
