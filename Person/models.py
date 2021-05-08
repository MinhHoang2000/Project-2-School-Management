from datetime import datetime
from django.db import models
import uuid
from django.utils import timezone
# Create your models here.

class Person(models.Model):
    id = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4, primary_key=True, editable=False)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    date_of_birth = models.DateField(null=True)
    religion = models.CharField(max_length=250,null=True)
    email = models.EmailField(max_length=250,null=True)
    address = models.CharField(max_length=250,null=True)
    phone = models.IntegerField(null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('FM', 'Female'),
    )
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)

    class Meta:
        db_table = "person"

    def __str__(self):
        return self.last_name+ ' ' + self.first_name

# Thành tựu
class Achievement(models.Model):
    id = models.AutoField(primary_key=True)
    achievement_name = models.CharField(max_length=250)
    created_at = models.DateField(default=datetime.now)

    class Meta:
        db_table = 'achievement'
# Hồ sơ sức khỏe
class Health(models.Model):
    id = models.AutoField(primary_key=True)
    height = models.SmallIntegerField()
    weight = models.SmallIntegerField()
    eye_sight = models.SmallIntegerField()
    health_status = models.TextField(null=True)
    disease = models.TextField(null=True)

    class Meta:
        db_table = 'health'