from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)
    stars = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images/")
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, blank=True, null=True
    )

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="categories/")

    is_popular = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name


class AboutUs(models.Model):
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField(max_length=100)
    address_url = models.TextField(null=True)
    telegram = models.CharField(max_length=30)
    facebook = models.CharField(max_length=30)
    instagram = models.CharField(max_length=30)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.id)


class Banner(models.Model):
    name = models.CharField(max_length=150)
    link = models.URLField()
    image = models.ImageField(upload_to="banner_image/")

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    products = models.ManyToManyField(Product, related_name="product_orders")
    quantity = models.IntegerField(default=0)

    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=14)
    delivery_address = models.TextField()

    total_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    delivery_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.full_name
