# Generated by Django 3.1.7 on 2021-03-28 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_orders_items_json'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='address1',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='address2',
        ),
    ]
