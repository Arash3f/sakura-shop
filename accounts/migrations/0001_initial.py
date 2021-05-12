# Generated by Django 3.2 on 2021-05-12 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('national_code', models.IntegerField(blank=True, null=True, verbose_name='national_code')),
                ('phone', models.IntegerField(blank=True, null=True, verbose_name='phone number')),
                ('money', models.IntegerField(default=0, verbose_name='money')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='date of birth')),
                ('registration_date', models.DateField(auto_now_add=True, verbose_name='registration date')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='users_picture/', verbose_name='picture')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]