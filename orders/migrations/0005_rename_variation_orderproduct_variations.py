# Generated by Django 3.2 on 2021-06-29 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_rename_variations_orderproduct_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='variation',
            new_name='variations',
        ),
    ]
