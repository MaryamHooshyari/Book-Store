from .models.category import Category


def categories(request):
    return {
        'default_categories': Category.objects.all().order_by('id')
    }
