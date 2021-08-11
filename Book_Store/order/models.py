from django.db import models
from product.models import Book
from user.models import Customer


# todo: count total price of orders!
class Order(models.Model):
    """
    Order model:
    ADDRESS_CHOICES: choice field contains all addresses belongs to owner
    """
    ADDRESS_CHOICES = 'Customer.addresses'
    STATUS_CHOICES = [('0', 'in progress'),
                      ('1', 'registered')]

    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, related_name='orders')
    address = models.CharField(max_length=300, choices=ADDRESS_CHOICES)
    register_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='0')
    created = models.DateTimeField(auto_now_add=True)
    # total_price = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.owner.username} {self.status} on {self.register_date}'


class OrderDetail(models.Model):
    """
    Order Detail model:
    shows how many of which product exist in which order!
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='details')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='details')
    number_of_books = models.PositiveIntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def price(self):
        return self.number_of_books * self.book.price

    def __str__(self):
        return f'{self.number_of_books} of {self.book.title}'
