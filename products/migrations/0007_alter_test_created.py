# Generated by Django 4.1.7 on 2023-02-19 12:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_test_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
