# Generated by Django 3.2 on 2021-06-14 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_auto_20210614_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productgallery',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='product.product'),
        ),
    ]
