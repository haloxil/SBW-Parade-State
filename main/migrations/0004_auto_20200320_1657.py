# Generated by Django 3.0.4 on 2020-03-20 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200319_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
