# Generated by Django 3.0.4 on 2020-03-22 13:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20200322_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 22, 21, 29, 39, 360816)),
        ),
    ]