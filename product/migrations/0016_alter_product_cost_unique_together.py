# Generated by Django 3.2 on 2021-05-22 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_auto_20210522_1043'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='product_cost',
            unique_together={('product', 'pack')},
        ),
    ]
