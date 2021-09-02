from datetime import datetime

import pytz

from django.db import models
from product.models.book import Book


class BookDiscount(models.Model):
    """
    Percent Off model:
    reduces the price of books by a percentage
    this will directly affect the book
    """

    class Meta:
        verbose_name = 'تخفیف کتاب'
        verbose_name_plural = 'تخفیف های کتاب'

    start_date = models.DateTimeField()
    expire_date = models.DateTimeField()
    percent = models.IntegerField()
    amount = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_off')
    created = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        if self.start_date < datetime.now(pytz.timezone('Asia/Tehran')) < self.expire_date:
            return True
        else:
            return False

    @property
    def discount_price(self):
        if self.is_valid():
            percentage = (self.book.unit_price * self.percent) / 100
            if self.book.unit_price - percentage > self.amount:
                result = percentage + self.amount
                return result
            else:
                return 0
        else:
            return 0

    def __str__(self):
        return f'{self.percent} percent off till {self.expire_date}'


# todo: add validator
class BonusDiscount(models.Model):
    """
    Bonus Off model:
    reduces the price of customer's order by a certain percentage up to a certain amount
    this will affect on the total price of orders
    """

    class Meta:
        verbose_name = 'تخفیف امتیازی'
        verbose_name_plural = 'تخفیف های امتیازی'

    coupon = models.CharField(max_length=20, null=False, blank=False, unique=True)
    start_date = models.DateTimeField()
    expire_date = models.DateTimeField()
    amount = models.FloatField(blank=True, null=True)
    percent = models.FloatField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.percent} percent discount up to {self.amount} Tomans'

    def deactivate(self):
        self.is_active = False
        self.save()
