# Generated by Django 2.1.3 on 2018-11-29 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0002_basket_order_yn'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill',
            old_name='order_date',
            new_name='order_date_time',
        ),
    ]