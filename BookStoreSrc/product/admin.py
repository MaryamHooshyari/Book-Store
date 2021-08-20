from django.contrib import admin
from .models.book import Book
from .models.category import Category
from .models.author import Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'number_in_stock']
    list_editable = ['unit_price', 'number_in_stock']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
