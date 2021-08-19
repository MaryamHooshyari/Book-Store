from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.defaultfilters import slugify


class CustomUser(AbstractUser):
    """
    CustomUser model:
    my base user model
    """
    email = models.EmailField(unique=True)
    slug = models.SlugField(null=False, allow_unicode=True, unique=True)

    def __str__(self):
        return self.email

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
