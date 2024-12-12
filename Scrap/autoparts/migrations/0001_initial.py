# Generated by Django 5.1.4 on 2024-12-11 21:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Vehicle', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('name_en', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('name_en', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(default='parts_images/default.svg', upload_to='parts_images/')),
                ('part_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autoparts.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_direction', models.CharField(blank=True, choices=[('Right', 'يمين'), ('Left', 'يساد')], max_length=64, null=True)),
                ('made', models.CharField(blank=True, max_length=64, null=True)),
                ('stock', models.SmallIntegerField()),
                ('condition', models.CharField(max_length=255)),
                ('start_date', models.IntegerField()),
                ('end_date', models.IntegerField()),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=2000)),
                ('image', models.ImageField(blank=True, default='products_images/', upload_to='products_images/')),
                ('car', models.ManyToManyField(related_name='products', to='Vehicle.car')),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoparts.part')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='accounts.profileseller')),
            ],
        ),
    ]