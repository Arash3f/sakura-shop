# Generated by Django 3.2 on 2021-05-27 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_packs_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='show_cost',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='قیمت نمایشی'),
        ),
    ]