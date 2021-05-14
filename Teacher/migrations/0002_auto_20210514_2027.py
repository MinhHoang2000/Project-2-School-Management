# Generated by Django 3.1.7 on 2021-05-14 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Person', '0008_auto_20210507_2340'),
        ('Teacher', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='achievement',
        ),
        migrations.CreateModel(
            name='TeacherAchievement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('achievement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Person.achievement')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Teacher.teacher')),
            ],
            options={
                'db_table': 'teacher_achievement',
            },
        ),
    ]
