# Generated by Django 3.1.7 on 2021-04-26 15:37

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid5, editable=False, primary_key=True, serialize=False, unique=True)),
                ('achievement_name', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'achievement',
            },
        ),
        migrations.CreateModel(
            name='Health',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid5, editable=False, primary_key=True, serialize=False, unique=True)),
                ('height', models.SmallIntegerField()),
                ('weight', models.SmallIntegerField()),
                ('eye_sight', models.SmallIntegerField()),
                ('health_status', models.TextField(null=True)),
                ('disease', models.TextField(null=True)),
            ],
            options={
                'db_table': 'health',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid5, editable=False, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('date_of_birth', models.DateField()),
                ('religion', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('phone', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('FM', 'Female')], max_length=2)),
            ],
            options={
                'db_table': 'person',
            },
        ),
    ]
