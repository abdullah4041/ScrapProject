# Generated by Django 5.1.4 on 2024-12-17 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoparts', '0006_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='products_images/default.svg', upload_to='products_images/'),
        ),
    ]