# Generated by Django 3.2 on 2021-05-22 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_product_slug'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('slug', 'name')},
        ),
    ]
