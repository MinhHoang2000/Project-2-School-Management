# Generated by Django 3.1.7 on 2021-04-27 18:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_auto_20210427_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.CharField(blank=True, default=uuid.uuid4, editable=False, max_length=100, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='permission',
            name='id',
            field=models.CharField(blank=True, default=uuid.uuid4, editable=False, max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
