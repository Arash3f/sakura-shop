# Generated by Django 3.2 on 2021-06-13 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_alter_properties_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='product_properties', to='product.product', verbose_name='خواص'),
        ),
    ]
