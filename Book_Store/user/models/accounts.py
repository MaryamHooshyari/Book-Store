from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    CustomUser model:
    my base user model
    """

    username = models.CharField(max_length=150, unique=False)
    email = models.EmailField(unique=True, blank=False)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super(CustomUser, self).save(*args, **kwargs)


class Employee(CustomUser):
    class Meta:
        proxy = True
        verbose_name = 'کارمند'
        verbose_name_plural = 'کارمندها'


class Customer(CustomUser):
    class Meta:
        proxy = True
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتری ها'
