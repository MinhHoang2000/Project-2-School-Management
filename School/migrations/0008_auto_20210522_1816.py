# Generated by Django 3.1.7 on 2021-05-22 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0002_auto_20210514_2027'),
        ('School', '0007_auto_20210522_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='studydocument',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='School.course'),
        ),
        migrations.AddField(
            model_name='studydocument',
            name='school_year',
            field=models.CharField(default='2021-2022', max_length=250),
        ),
        migrations.AddField(
            model_name='studydocument',
            name='semester',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='studydocument',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Teacher.teacher'),
        ),
    ]