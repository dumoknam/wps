# Generated by Django 2.1.3 on 2018-12-10 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0017_auto_20181210_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='item_type',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='description',
            name='receive_day',
            field=models.CharField(max_length=200),
        ),
    ]
