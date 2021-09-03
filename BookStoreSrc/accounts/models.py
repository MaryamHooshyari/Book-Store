from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class CustomUser(AbstractUser):
    """
    CustomUser model:
    my base user model
    """
    email = models.EmailField(unique=True)
    slug = models.SlugField(null=False, allow_unicode=True, unique=True)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.email[:len(str(self.email)) - 3])
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


class Address(models.Model):
    class Meta:
        verbose_name = 'آدرس'
        verbose_name_plural = 'آدرس ها'

    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='address')
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    town = models.CharField(max_length=50, blank=True, null=True)
    street = models.CharField(max_length=50)
    postal_code = models.IntegerField(blank=True, null=True)
    details = models.CharField(max_length=200, blank=True, null=True)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.owner.username} از {self.city} در {self.state}'
