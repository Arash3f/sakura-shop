# Generated by Django 3.2 on 2021-05-27 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20210525_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='packs',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.packs', verbose_name='نوع'),
        ),
    ]