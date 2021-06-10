# Generated by Django 3.2 on 2021-05-31 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_product_group_open'),
        ('shop', '0002_auto_20210531_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderrow',
            name='pack',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='product.product_cost'),
            preserve_default=False,
        ),
    ]