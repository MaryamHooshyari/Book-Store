from accounts.models import Address, Customer
from discount.models import BonusDiscount
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
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, blank=True, null=True)
    discount_code = models.CharField(max_length=50, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.status} برای {self.owner.username}'

    @property
    def original_price(self):
        """
        return: <int>
        """
        return sum(item.item_price for item in self.items.all())

    def discount(self):
        """
        calculate discount on percent up to a certain amount
        return: <int, float>
        """
        if self.discount_code:
            all_discounts = BonusDiscount.objects.all()
            for dis in all_discounts:
                if self.discount_code == dis.coupon:
                    my_discount = dis
                    if my_discount.is_valid():
                        discount_amount = (self.original_price * my_discount.percent) / 100
                        if discount_amount > my_discount.amount:
                            return my_discount.amount
                        else:
                            return discount_amount
                    else:
                        return 0
        else:
            return 0

    @property
    def final_price(self):
        """
        return: <int, float>
        """
        return self.original_price - self.discount()


class OrderItem(models.Model):
    """
    Order Item model:
    shows how many of which product exist in which order!
    """

    class Meta:
        verbose_name = 'جزییات سفارش'
        verbose_name_plural = 'جزییات سفارش ها'

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='booksInItems')
    quantity = models.PositiveIntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def item_price(self):
        """
        return: <int>
        """
        return self.quantity * self.book.final_price

    def __str__(self):
        return f'{self.quantity} of {self.book.title}'
