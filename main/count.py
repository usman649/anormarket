from .models import Order

def cart_count_processor(request):
    total_items = sum(order.quantity for order in Order.objects.all())
    return {'cart_total_count': total_items}
