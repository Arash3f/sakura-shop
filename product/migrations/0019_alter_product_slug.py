# Generated by Django 3.2 on 2021-05-22 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_alter_product_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=255, unique=True),
        ),
    ]