# Generated by Django 2.1.3 on 2018-11-29 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0009_auto_20181128_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='sale_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
