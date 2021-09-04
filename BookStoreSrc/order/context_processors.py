from .models import Order


def cart(request):
    if not request.user.is_anonymous:
        return {
            'basket': Order.objects.filter(owner=request.user).get(status='سبد خرید')
        }
    else:
        return {
            'basket': Order.objects.all().first()
        }
