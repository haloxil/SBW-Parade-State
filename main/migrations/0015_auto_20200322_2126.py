# Generated by Django 3.0.4 on 2020-03-22 13:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20200322_2121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='name',
        ),
        migrations.AddField(
            model_name='person',
            name='rank',
            field=models.CharField(choices=[('REC', 'REC'), ('PTE', 'PTE'), ('LCP', 'LCP'), ('CPL', 'CPL'), ('CFC', 'CFC'), ('3SG', '3SG'), ('2SG', '2SG'), ('1SG', '1SG'), ('SSG', 'SSG'), ('MSG', 'MSG'), ('3WO', '3WO'), ('2WO', '2WO'), ('1WO', '1WO'), ('MAJ', 'MAJ'), ('DX06', 'DX06'), ('DX07', 'DX07'), ('DX10', 'DX10')], default='PTE', max_length=30),
        ),
        migrations.AlterField(
            model_name='person',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 22, 21, 26, 29, 615706)),
        ),
        migrations.AlterField(
            model_name='person',
            name='status',
            field=models.CharField(choices=[('Present', 'Present'), ('Present Event', 'Present Event'), ('Present Work', 'Present Work'), ('AL', 'AL'), ('OL', 'OL'), ('OIL', 'OIL'), ('RSO', 'RSO'), ('RSI', 'RSI'), ('MA', 'MA'), ('MC', 'MC'), ('OA', 'OA'), ('AO', 'AO'), ('CSE', 'CSE'), ('OOC', 'OOC')], default='Present', max_length=30),
        ),
    ]
