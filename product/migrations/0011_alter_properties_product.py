# Generated by Django 3.2 on 2021-06-13 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20210613_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='product_properties', to='product.product', verbose_name='خواص'),
        ),
    ]