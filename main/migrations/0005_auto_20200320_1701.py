# Generated by Django 3.0.4 on 2020-03-20 09:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200320_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 20, 17, 1, 21, 652664)),
        ),
    ]
