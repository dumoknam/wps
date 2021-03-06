# Generated by Django 2.1.3 on 2018-11-27 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_category', models.CharField(max_length=30)),
                ('sub_category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_words', models.CharField(blank=True, max_length=200, null=True)),
                ('point', models.IntegerField(default=0)),
                ('delivery_type', models.CharField(max_length=200)),
                ('receive_day', models.CharField(max_length=100)),
                ('item_type', models.CharField(max_length=50)),
                ('factory_address', models.TextField()),
                ('dom', models.CharField(max_length=50)),
                ('capacity', models.CharField(max_length=30)),
                ('ingredient', models.TextField()),
                ('allergy_material', models.TextField()),
                ('caution', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=150)),
                ('company', models.CharField(max_length=50)),
                ('origin_price', models.IntegerField()),
                ('sale_price', models.IntegerField()),
                ('discount_rate', models.FloatField(default=0.0)),
                ('categories', models.ManyToManyField(to='items.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_type', models.CharField(choices=[('T', 'thumbnail'), ('D', 'detail'), ('L', 'list_thumbnail')], max_length=1)),
                ('image_order', models.IntegerField()),
                ('photo', models.ImageField(upload_to='ItemImage')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Item')),
            ],
        ),
        migrations.AddField(
            model_name='description',
            name='item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='items.Item'),
        ),
    ]
