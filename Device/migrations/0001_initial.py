# Generated by Django 3.1.7 on 2021-04-26 15:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceInfo',
            fields=[
                ('id', models.CharField(blank=True, default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('device_name', models.CharField(max_length=250)),
                ('device_status', models.CharField(choices=[('N', 'Normal'), ('B', 'Broken'), ('BB', 'Be Borrowed')], max_length=2)),
            ],
            options={
                'db_table': 'device',
            },
        ),
        migrations.CreateModel(
            name='DeviceMan',
            fields=[
                ('id', models.CharField(blank=True, default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('day_of_week', models.CharField(choices=[('2', 'Thứ 2'), ('3', 'Thứ 3'), ('4', 'Thứ 4'), ('5', 'Thứ 5'), ('6', 'Thứ 6'), ('7', 'Thứ 7')], max_length=3)),
                ('shift', models.CharField(choices=[('M1', '7:15-8:00'), ('M2', '8:10-8:55'), ('M3', '9:05-9:50'), ('M4', '10:05-10:50'), ('M5', '11:00-11:45'), ('A1', '13:00-13:45'), ('A2', '13:55-14:10'), ('A3', '14:50-15:35'), ('A4', '15:50-16:35'), ('A5', '16:45-17:30')], max_length=2)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Device.deviceinfo')),
            ],
            options={
                'db_table': 'device_manage',
            },
        ),
    ]