from django.db import models
from django.contrib.auth.models import User


def format_vnd(price):
    # Ensure price is numeric
    try:
        price = float(price)
    except (TypeError, ValueError):
        return price

    # Format the price as VND
    formatted_price = "{:,.0f}".format(price)
    return formatted_price


def deleteComma(price):
    if isinstance(price, str):
        return price.replace(",", "")
    else:
        return price


class Customer(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE, related_name="customer"
    )
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    purchase = models.IntegerField(default=1, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=550)
    description = models.TextField(null=True, blank=True)
    new_price = models.IntegerField()
    old_price = models.IntegerField()
    quantity = models.IntegerField(default=0, null=True, blank=True)
    brand = models.TextField(default="No band", null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    digital = models.BooleanField(default=False, null=True, blank=True)
    sold = models.IntegerField(default=0, null=True, blank=True)
    purchase = models.ForeignKey(
        Purchase, default=1, null=True, blank=True, on_delete=models.SET_DEFAULT
    )

    def __str__(self):
        return self.name

    def persent(self):
        persent = (
            (int(deleteComma(self.old_price)) - int(deleteComma(self.new_price)))
            / int(deleteComma(self.old_price))
        ) * 100
        return round(persent)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url


class Order(models.Model):
    customer = models.ForeignKey(
        Customer,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    date_ordered = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def address(self):
        address = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                address = True
        return address

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([int(deleteComma(item.get_total)) for item in orderitems])
        totalFormat = format_vnd(total)
        return totalFormat

    @property
    def get_cart_quantity(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        new_price = self.product.new_price
        new_price_str = deleteComma(new_price)

        total = int(new_price_str) * self.quantity
        totalFormat = format_vnd(total)
        return totalFormat


class DeliveryAddress(models.Model):
    customer = models.ForeignKey(
        Customer,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.SET_NULL)
    phone = models.IntegerField(null=True)
    address = models.CharField(max_length=255, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
