# Generated by Django 2.0.1 on 2018-04-05 15:20

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_product_in_cart_session_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default=None, max_length=128, null=True),
        ),
    ]
