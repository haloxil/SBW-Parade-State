# Generated by Django 3.0.4 on 2020-03-21 05:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20200321_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 21, 13, 21, 55, 220551)),
        ),
    ]
