# Generated by Django 4.0.1 on 2022-01-10 03:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_complete_mymodel_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 10, 3, 27, 43, 61075, tzinfo=utc)),
        ),
    ]
