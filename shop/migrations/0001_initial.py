# Generated by Django 3.2 on 2021-05-31 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0007_product_group_open'),
        ('accounts', '0002_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_time', models.DateTimeField(null=True)),
                ('status', models.IntegerField(choices=[(1, 'در حال خرید'), (2, 'ثبت\u200cشده'), (3, 'لغوشده'), (4, 'ارسال\u200cشده')])),
                ('total_price', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.users')),
            ],
        ),
        migrations.CreateModel(
            name='OrderRow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rows', to='shop.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product')),
            ],
        ),
    ]