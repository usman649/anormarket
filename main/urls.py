from django.urls import path
from .views import home_view,product_view,category_view,cart_view,category_detail_view,cart_detail_view,cart_delete_view,search_view,checkout_view,about_us_view

urlpatterns = [
    path("", home_view, name="home"),
    path("product/<int:pk>/", product_view, name="product"),
    path("category/", category_view, name="category"),
    path("category/<int:pk>/", category_detail_view, name="category_detail"),
    path("cart/", cart_view, name="cart"),
    path('cart/detail/',cart_detail_view, name="cart_detail"),
    path('cart/delete/',cart_delete_view, name="cart_delete"),
    path('search/', search_view, name="search"),
    path('checkout/', checkout_view, name="checkout"),
    path('about/', about_us_view, name="about"),


]
