# Generated by Django 3.1.7 on 2021-05-02 15:09

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0006_auto_20210501_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(error_messages={'unique': 'Username already exists'}, max_length=128, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()]),
        ),
    ]