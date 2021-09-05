from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

from BookStoreSrc.settings import BASE_DIR
from order.models import Order

import pytz

from ..models import CustomUser


def admin_report(request):
    customer_no = CustomUser.objects.filter(is_staff=False).count()
    staff_no = CustomUser.objects.filter(is_staff=True).filter(is_superuser=False).count()
    today = datetime.now(pytz.timezone('Asia/Tehran')).date()
    today_checked = CustomUser.objects.filter(is_staff=False).filter(last_login__date=today).count()
    today_orders = Order.objects.filter(status='ثبت شده', updated__date=today)
    context = {
        'customer_no': customer_no,
        'staff_no': staff_no,
        'today_checked': today_checked,
        'today_orders': today_orders,
    }
    return render(request, 'admin/admin_report.html', context)


def json_download_today_submit_orders(request):
    # find all today submitted orders
    today = datetime.now(pytz.timezone('Asia/Tehran')).date()
    objects = Order.objects.filter(status='ثبت شده', updated__date=today)
    # save 'today_orders' to a file in json style
    with open(str(BASE_DIR) + '/today_orders.json', "w", encoding='utf-8') as out:
        json_orders = serializers.serialize("json", objects)
        out.write(json_orders)
    file_orders = open(str(BASE_DIR) + '/today_orders.json', 'rb')
    response = HttpResponse(file_orders, content_type='json')
    response['Content-Disposition'] = "attachment; filename=today_orders.json" % objects
    return response
