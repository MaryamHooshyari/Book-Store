from .models import Order


def cart(request):
    if not request.user.is_anonymous:
        if not request.user.is_staff:
            return {
                'basket': Order.objects.filter(owner=request.user).get(status='سبد خرید')
            }
    return {
        'basket': Order.objects.all().first()
    }
