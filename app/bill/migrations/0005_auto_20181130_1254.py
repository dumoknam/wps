# Generated by Django 2.1.3 on 2018-11-30 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0004_auto_20181129_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='sale_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
