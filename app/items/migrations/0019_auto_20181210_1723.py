# Generated by Django 2.1.3 on 2018-12-10 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0018_auto_20181210_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='dom',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='description',
            name='item_type',
            field=models.CharField(max_length=2000),
        ),
    ]
