# Generated by Django 3.2 on 2021-05-21 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True, verbose_name='وضعیت'),
            preserve_default=False,
        ),
    ]