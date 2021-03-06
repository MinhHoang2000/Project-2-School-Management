# Generated by Django 3.1.7 on 2021-04-26 15:37

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Account', '0001_initial'),
        ('Person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.CharField(blank=True, default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('account', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Account.account')),
                ('achievement', models.ManyToManyField(to='Person.Achievement')),
                ('personal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Person.person')),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
    ]
