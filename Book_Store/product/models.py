from django.db import models


class Category(models.Model):
    """
    Category model:
    it has many to many relation with Book model
    """

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Author(models.Model):
    """
    Author model:
    it has many to many relation with Book model
    """

    class Meta:
        verbose_name = 'نویسنده'
        verbose_name_plural = 'نویسنده ها'

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


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
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def calculate_final_price(self):
        result = self.unit_price - self.book_off.discount_price
        return result
