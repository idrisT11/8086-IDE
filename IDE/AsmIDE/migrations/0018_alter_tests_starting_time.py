# Generated by Django 3.2 on 2021-05-08 00:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('AsmIDE', '0017_alter_tests_starting_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tests',
            name='starting_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 0, 8, 15, 990747, tzinfo=utc)),
        ),
    ]