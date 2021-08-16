from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from .author import Author
from .category import Category


class Book(models.Model):
    """
    Book model:
    """

    class Meta:
        verbose_name = 'کتاب'
        verbose_name_plural = 'کتاب ها'

    title = models.CharField(max_length=100)
    number_in_stock = models.PositiveIntegerField()
    authors = models.ManyToManyField(Author, related_name='books')
    categories = models.ManyToManyField(Category, related_name='books')
    unit_price = models.PositiveIntegerField()
    slug = models.SlugField(null=False, unique=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def calculate_final_price(self):
        result = self.unit_price - self.book_off.discount_price
        return result

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
