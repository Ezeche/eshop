# Generated by Django 4.1 on 2022-09-08 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_remove_customer_useraddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='postal_code',
            field=models.CharField(default=None, max_length=12),
        ),
    ]
