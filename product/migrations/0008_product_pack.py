# Generated by Django 3.2 on 2021-05-22 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_comment_packs'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pack',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.packs', verbose_name='بسته'),
            preserve_default=False,
        ),
    ]
