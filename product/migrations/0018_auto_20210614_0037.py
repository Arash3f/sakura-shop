# Generated by Django 3.2 on 2021-06-14 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_alter_productgallery_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productgallery',
            options={'verbose_name': 'عکس ', 'verbose_name_plural': 'عکس ها'},
        ),
        migrations.AddField(
            model_name='product_group',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='product_group/', verbose_name='عکس'),
        ),
        migrations.AlterField(
            model_name='productgallery',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='picture', to='product.product'),
        ),
    ]