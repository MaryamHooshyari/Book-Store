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
    authors = models.ManyToManyField(Author, related_name='book_author')
    categories = models.ManyToManyField(Category, related_name='book_category')
    unit_price = models.IntegerField()
    # final_price = models.IntegerField(default=0)
    slug = models.SlugField(null=False, allow_unicode=True, unique=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def final_price(self):
        total_discount = 0
        for x in self.book_off.all():
            total_discount += x.discount_price
        if self.unit_price > total_discount:
            return int(self.unit_price - total_discount)

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        # total_discount = 0
        # for x in self.book_off.all():
        #     total_discount += x.discount_price
        # if self.unit_price > total_discount:
        #     self.final_price = self.unit_price - total_discount
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
