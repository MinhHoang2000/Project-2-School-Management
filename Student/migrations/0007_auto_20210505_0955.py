# Generated by Django 3.1.7 on 2021-05-05 09:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0001_initial'),
        ('Person', '0003_auto_20210503_1651'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Student', '0006_auto_20210505_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='account',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='student',
            name='classroom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='School.classroom'),
        ),
        migrations.AlterField(
            model_name='student',
            name='health',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Person.health'),
        ),
    ]
