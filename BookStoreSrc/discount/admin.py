from django.contrib import admin
from .models import BookDiscount, BonusDiscount

admin.site.register(BookDiscount)
admin.site.register(BonusDiscount)
