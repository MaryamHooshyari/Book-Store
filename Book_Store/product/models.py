from django.db import models


class Category(models.Model):
    """
    Category model:
    it has many to many relation with Book model
    """
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Author(models.Model):
    """
    Author model:
    it has many to many relation with Book model
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    """
    Book model:
    """
    title = models.CharField(max_length=100)
    number_in_stock = models.PositiveIntegerField()
    authors = models.ManyToManyField(Author, related_name='books')
    categories = models.ManyToManyField(Category, related_name='books')
    price = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
