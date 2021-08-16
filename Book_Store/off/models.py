import pytz
from datetime import datetime

from django.db import models
from product.models.book import Book


class BookOff(models.Model):
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
    percent = models.FloatField()
    amount = models.FloatField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_off')
    created = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        pass
        # if self.start_date < datetime.now(pytz.timezone('Asia/Tehran') < self.expire_date:
        #     return True
        # else:
        #     return False

    @property
    def discount_price(self):
        if self.book.unit_price > self.amount:
            result = ((self.book.unit_price - self.amount) * (100 - self.percent)) / 100
            return result
        else:
            return 0

    def __str__(self):
        return f'{self.percent} percent off till {self.expire_date}'


# todo: add validator
class BonusOff(models.Model):
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
