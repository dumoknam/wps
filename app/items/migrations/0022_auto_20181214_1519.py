# Generated by Django 2.1.3 on 2018-12-14 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0021_auto_20181212_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
    ]
