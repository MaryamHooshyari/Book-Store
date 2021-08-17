from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Author(models.Model):
    """
    Author model:
    it has many to many relation with Book model
    """

    class Meta:
        verbose_name = 'نویسنده'
        verbose_name_plural = 'نویسنده ها'

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(null=False, unique=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.full_name)
        return super().save(*args, **kwargs)
