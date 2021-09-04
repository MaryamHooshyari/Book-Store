from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from .models.author import Author
from .models.book import Book
from .models.category import Category


@admin.action(description='10 تا به موجودی اضافه کن')
def ten_plus(modeladmin, request, queryset):
    for obj in queryset:
        obj.number_in_stock += 10
        obj.save()


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'number_in_stock', 'final_price']
    list_editable = ['unit_price', 'number_in_stock']
    list_filter = (
        ('authors', admin.RelatedOnlyFieldListFilter),
        ('categories', admin.RelatedOnlyFieldListFilter),
    )
    prepopulated_fields = {'slug': ('title',)}
    actions = [ten_plus]


class BookCategoryInline(admin.TabularInline):
    model = Category.book_category.through
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [BookCategoryInline]
    prepopulated_fields = {'slug': ('name',)}


class BookAuthorInline(admin.TabularInline):
    model = Author.book_author.through
    extra = 0


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookAuthorInline]
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
