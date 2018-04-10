# Generated by Django 2.0.1 on 2018-04-10 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_remove_product__price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_active',
        ),
        migrations.AddField(
            model_name='product',
            name='in_stock',
            field=models.IntegerField(default=1),
        ),
    ]