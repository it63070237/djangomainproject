# Generated by Django 3.2.6 on 2021-09-29 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20210929_1939'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='link',
            new_name='firm_url',
        ),
    ]