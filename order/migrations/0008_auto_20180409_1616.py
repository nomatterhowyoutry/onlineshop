# Generated by Django 2.0.1 on 2018-04-09 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20180409_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_in_cart',
            name='currency',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='product_in_order',
            name='currency',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
    ]