# Generated by Django 3.0.4 on 2020-04-20 09:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20200420_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 17, 10, 40, 939116)),
        ),
    ]
