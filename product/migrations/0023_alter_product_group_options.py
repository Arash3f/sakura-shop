# Generated by Django 3.2 on 2021-05-24 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_product_group_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product_group',
            options={'ordering': ['-group'], 'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
    ]
