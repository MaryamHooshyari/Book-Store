from .models.category import Category


def categories(request):
    return {
        'categories': Category.objects.all()
    }
