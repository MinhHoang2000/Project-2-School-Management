# Generated by Django 3.1.7 on 2021-05-03 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Person', '0003_auto_20210503_1651'),
        ('Student', '0002_auto_20210428_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='health',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Person.health'),
        ),
    ]
