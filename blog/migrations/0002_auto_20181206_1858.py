# Generated by Django 2.1.4 on 2018-12-06 17:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 6, 17, 58, 25, 951334, tzinfo=utc)),
        ),
    ]