from .models.category import Category


# todo:add most used categories to this function return!
def categories(request):
    return {
        'default_categories': Category.objects.all().order_by('id')[:4]
    }
