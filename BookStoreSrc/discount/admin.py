from django.contrib import admin

from .models import BonusDiscount, BookDiscount

admin.site.register(BookDiscount)
admin.site.register(BonusDiscount)
