# Generated by Django 3.2.6 on 2021-09-29 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='link',
            field=models.URLField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]