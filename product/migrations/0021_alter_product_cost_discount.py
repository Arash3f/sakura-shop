# Generated by Django 3.2 on 2021-05-22 15:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_auto_20210522_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_cost',
            name='discount',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(99)], verbose_name='تخفیف'),
        ),
    ]