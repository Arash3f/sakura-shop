# Generated by Django 3.2 on 2021-06-09 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_orderrow_pack'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderrow',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
