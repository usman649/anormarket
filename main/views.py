from django.shortcuts import render,redirect
from .models import Product,Banner,Category,Order,AboutUs

def home_view(request):
    product = Product.objects.all()
    banner = Banner.objects.all()
    new_product = Product.objects.all().order_by('-created_at')
    on_sale = Product.objects.filter(status=True)
    category = Category.objects.filter(is_popular=True)
    d  = {
        'product': product,
        'banner': banner,
        'new_product': new_product,
        'on_sale': on_sale,
        'category': category,
    }
    return render(request, 'home.html',context=d)



def product_view(request,pk):
    product = Product.objects.filter(id=pk).first()
    d = {
        'product': product,
    }
    return render(request, 'product.html',context=d)


def category_view(request):
    category = Category.objects.all()
    d = {
        'category': category,
    }
    return render(request, 'category.html',context=d)

def category_detail_view(request,pk):
    category = Category.objects.filter(id=pk)
    d = {
        'category': category,

    }
    return render(request, 'category.html',context=d)


def search_view(request):
    if request.method == "POST":
        query = request.POST.get('query')

        product = Product.objects.filter(
            name__icontains=query
        )
        d = {
            'product': product,
        }


    return render(request, 'search.html',context=d)


def cart_view(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))

        product = Product.objects.filter(id=product_id).first()

        if product:
            existing_order = Order.objects.filter(user=request.user, products=product).first()

            if existing_order:
                existing_order.quantity += quantity
                existing_order.total_price += product.price * quantity
                existing_order.save()
            else:
                order = Order.objects.create(
                    user=request.user,
                    quantity=quantity,
                    total_price=product.price * quantity
                )
                order.products.add(product)

        return redirect('/')

    return redirect('/')


def cart_detail_view(request):
    order = Order.objects.all()
    grand_total = sum(order.total_price for order in order)
    d = {
        'order': order,
        'grand_total': grand_total,
    }
    return render(request, 'cart.html',context=d)

def checkout_view(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        delivery_address = request.POST.get('delivery_address')

        Order.objects.filter(user=request.user).update(
            full_name=full_name,
            phone_number=phone_number,
            delivery_address=delivery_address
        )

        return redirect('/')
    return redirect('/cart/detail/')


def cart_delete_view(request):
    if request.method == "POST":
        order_id = request.POST.get('order_id')

        if order_id:
            order = Order.objects.filter(id=order_id, user=request.user).first()

            if order:
                order.delete()

    return redirect('/cart/detail/')

def about_us_view(request):
    about = AboutUs.objects.first()
    d = {
        'about': about,
    }
    return render(request, 'about_us.html',context=d)
