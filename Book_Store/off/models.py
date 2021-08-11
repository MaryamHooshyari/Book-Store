from django.db import models
from product.models import Book
from user.models import Customer


class PercentOff(models.Model):
    """
    Percent Off model:
    reduces the price of books by a percentage
    this will directly affect the book
    """
    start_date = models.DateTimeField()
    expire_date = models.DateTimeField()
    percent = models.FloatField()
    books = models.ManyToManyField(Book, related_name='percent_off')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.percent} percent off till {self.expire_date}'


class AmountOff(models.Model):
    """
    Amount Off model:
    reduces the price of books by a certain amount
    this will directly affect the book
    """
    start_date = models.DateTimeField()
    expire_date = models.DateTimeField()
    amount = models.FloatField()
    books = models.ManyToManyField(Book, related_name='amount_off')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.amount} Tomans off till {self.expire_date}'


class BonusOff(models.Model):
    """
    Bonus Off model:
    reduces the price of customer's order by a certain percentage up to a certain amount
    this will affect on the total price of orders
    """
    off_code = models.CharField(max_length=20, null=False, blank=False)
    start_date = models.DateTimeField()
    expire_date = models.DateTimeField()
    amount = models.FloatField(blank=True, null=True)
    percent = models.FloatField(blank=True, null=True)
    customers = models.ManyToManyField(Customer, related_name='bonus_off')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.percent} percent discount up to {self.amount} Tomans'
