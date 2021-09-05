from .models import Order


def cart(request):
    if not request.user.is_anonymous:
        if not request.user.is_staff:
            try:
                basket = Order.objects.filter(owner=request.user).get(status='سبد خرید')
                basket_qty = basket.items.count()
            except:
                basket_qty = 0
            return {
                'basket': basket_qty
            }
    return {
        'basket': 0
    }
