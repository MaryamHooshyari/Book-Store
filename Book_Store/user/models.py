from django.db import models
from django.contrib.auth.models import AbstractUser


class Admin(AbstractUser):
    """
    Admin model:
    this is just for the super user
    """
    email = models.EmailField(unique=True, blank=False)

    def __str__(self):
        return self.email


class Employee(Admin):
    class Meta:
        verbose_name = 'Employee'


class Address(models.Model):
    city = models.CharField(max_length=40)
    street = models.CharField(max_length=50)
    details = models.CharField(max_length=300)

    # owner = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='addresses')

    def __str__(self):
        return f'{self.city} on {self.street}'


class Customer(Admin):
    class Meta:
        verbose_name = 'Customer'

    address = models.ManyToManyField(Address, related_name='addresses', blank=False)
