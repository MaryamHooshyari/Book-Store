# Generated by Django 3.2.6 on 2021-09-02 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdiscount',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bookdiscount',
            name='percent',
            field=models.IntegerField(),
        ),
    ]
