from datetime import datetime

import pytz

from accounts.models import Customer
from django.db import models
from product.models.book import Book


class Order(models.Model):
    """
    Order model:
    """

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارش ها'

    STATUS_CHOICES = [('سبد خرید', 'سبد خرید'),
                      ('سفارش', 'سفارش'),
                      ('ثبت شده', 'ثبت شده')]

    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True, related_name='orders')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='سبد خرید')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.status} for {self.owner.username}'

    def original_price(self):
        """
        return: <int>
        """
        return sum(item.price for item in self.items.all())

    def discount(self):
        """
        calculate discount on percent up to a certain amount
        return: <int, float>
        """
        off = self.owner.bonus_off.filter(expire_date__gt=datetime.now(pytz.timezone('Asia/Tehran')))
        if off.count() == 0:
            return 0
        else:
            result = (self.original_price() * off[0].percent) / 100
            if result < off[0].amount:
                return result
            else:
                return off[0].amount

    @property
    def final_price(self):
        """
        return: <int, float>
        """
        return self.original_price() - self.discount()


class OrderItem(models.Model):
    """
    Order Item model:
    shows how many of which product exist in which order!
    """

    class Meta:
        verbose_name = 'جزییات سفارش'
        verbose_name_plural = 'جزییات سفارش ها'

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='booksInItems')
    quantity = models.PositiveIntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def item_price(self):
        """
        return: <int>
        """
        return self.quantity * self.book.unit_price

    def __str__(self):
        return f'{self.quantity} of {self.book.title}'
