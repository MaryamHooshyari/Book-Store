from django.db import models
from .accounts import Customer


class Address(models.Model):
    class Meta:
        verbose_name = 'آدرس'
        verbose_name_plural = 'آدرس ها'

    city = models.CharField(max_length=40)
    street = models.CharField(max_length=50)
    details = models.CharField(max_length=300)
    is_default = models.BooleanField(default=True)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='address')

    def __str__(self):
        return f'{self.city} on {self.street}'
