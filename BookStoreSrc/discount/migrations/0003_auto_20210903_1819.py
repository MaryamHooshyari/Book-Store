# Generated by Django 3.2.6 on 2021-09-03 13:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0002_auto_20210902_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='bonusdiscount',
            name='limited_count',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='bonusdiscount',
            name='amount',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='bonusdiscount',
            name='percent',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='bookdiscount',
            name='amount',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='bookdiscount',
            name='percent',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)]),
        ),
    ]
