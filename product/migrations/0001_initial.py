# Generated by Django 3.2 on 2021-05-25 19:28

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='packs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='عنوان')),
                ('weight', models.IntegerField(verbose_name='اندازه')),
            ],
            options={
                'verbose_name': 'بسته ها',
                'verbose_name_plural': 'بسته',
            },
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='نام کالا')),
                ('slug', models.SlugField(allow_unicode=True, max_length=255, unique=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='عکس')),
                ('inventory', models.PositiveIntegerField(verbose_name='موجودی')),
                ('available', models.BooleanField(default=True, verbose_name='(موجودی)وضعیت')),
                ('sell', models.IntegerField(blank=True, null=True, verbose_name='تعداد فروش')),
            ],
            options={
                'verbose_name': 'کالا',
                'verbose_name_plural': 'کالا ها',
                'unique_together': {('slug', 'name')},
            },
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.comment')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'نظر',
                'verbose_name_plural': 'نظرات',
            },
        ),
        migrations.CreateModel(
            name='product_cost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(99)], verbose_name='تخفیف')),
                ('available', models.BooleanField(default=True, verbose_name='(بسته)وضعیت')),
                ('cost', models.IntegerField(blank=True, null=True, verbose_name='قیمت')),
                ('pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_cost', to='product.packs', verbose_name='بسته')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_cost', to='product.product', verbose_name='کالا')),
            ],
            options={
                'verbose_name': 'قیمت',
                'verbose_name_plural': 'قیمت ها',
                'unique_together': {('product', 'pack')},
            },
        ),
    ]
