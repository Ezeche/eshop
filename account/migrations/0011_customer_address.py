# Generated by Django 4.1 on 2022-09-09 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_customer_postal_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default=None, max_length=100),
        ),
    ]