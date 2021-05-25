# Generated by Django 3.2 on 2021-05-21 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='inventory',
            field=models.PositiveIntegerField(default=100, verbose_name='موجودی'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True, verbose_name='وضعیت'),
        ),
    ]