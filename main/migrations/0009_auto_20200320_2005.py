# Generated by Django 3.0.4 on 2020-03-20 12:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200320_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 20, 20, 5, 26, 515737)),
        ),
        migrations.AlterField(
            model_name='person',
            name='status',
            field=models.CharField(choices=[('Present', 'Present'), ('Present Event', 'Present Event'), ('Present Work', 'Present Work'), ('AL', 'AL'), ('OL', 'OL'), ('OIL', 'OIL'), ('RSO', 'RSO'), ('RSI', 'RSI'), ('MA', 'MA'), ('MC', 'MC'), ('OA', 'OA'), ('AO', 'AO'), ('CSE', 'CSE'), ('OOC', 'OOC')], default='present', max_length=30),
        ),
    ]