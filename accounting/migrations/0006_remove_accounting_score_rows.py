# Generated by Django 3.2 on 2021-07-11 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0005_auto_20210711_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounting_score',
            name='rows',
        ),
    ]