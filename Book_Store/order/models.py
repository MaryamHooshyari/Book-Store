import pytz
from datetime import datetime
from django.db import models
from product.models import Book
from user.models.accounts import Customer


# todo: count total price of orders!
class Order(models.Model):
    """
    Order model:
    ADDRESS_CHOICES: choice field contains all addresses belongs to owner
    STATUS_CHOICES: has two values, 0 means still in progress and 1 means it has registered
    """

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارش ها'

    STATUS_CHOICES = [('0', 'in progress'),
                      ('1', 'registered')]

    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True, related_name='orders')
    # original_price = models.FloatField()
    # discount = models.FloatField()
    # final_price = models.FloatField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='0')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.status} on {self.updated}'

    def calculate_original_price(self):
        """
        return: <int>
        """
        detail_list = self.details.all()
        result = 0
        for dl in detail_list:
            result += dl.price
        return result

    def calculate_discount(self):
        """
        calculate discount on percent up to a certain amount
        return: <int, float>
        """
        off = self.owner.bonus_off.filter(expire_date__gt=datetime.now(pytz.timezone('Asia/Tehran')))
        if off.count() == 0:
            return 0
        else:
            result = (self.calculate_original_price() * off[0].percent) / 100
            if result < off[0].amount:
                return result
            else:
                return off[0].amount

    @property
    def calculate_final_price(self):
        """
        return: <int, float>
        """
        result = self.calculate_original_price() - self.calculate_discount()
        return result


class OrderDetail(models.Model):
    """
    Order Detail model:
    shows how many of which product exist in which order!
    """

    class Meta:
        verbose_name = 'جزییات سفارش'
        verbose_name_plural = 'جزییات سفارش ها'

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='details')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='details')
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def calculate_price(self):
        """
        return: <int>
        """
        result = self.quantity * self.book.price
        return result

    def __str__(self):
        return f'{self.quantity} of {self.book.title}'

    def save(self, *args, **kwargs):
        self.price = self.calculate_price()
        super(OrderDetail, self).save(*args, **kwargs)
