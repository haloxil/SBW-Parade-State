# Generated by Django 3.0.4 on 2020-03-19 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200319_2317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='nric',
            new_name='name',
        ),
    ]