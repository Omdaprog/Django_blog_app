# Generated by Django 2.1.4 on 2018-12-06 18:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181206_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 6, 18, 1, 25, 542791, tzinfo=utc)),
        ),
    ]
