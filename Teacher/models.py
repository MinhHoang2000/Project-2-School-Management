from django.db import models
import uuid

from django.db.models.fields import AutoField
from Person.models import Person, Achievement
from Account.models import Account

# Create your models here.

# Thông tin giáo viên
class Teacher(models.Model):
    id = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4, primary_key=True)
    personal = models.OneToOneField(Person, on_delete=models.CASCADE)
    account = models.OneToOneField(Account, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "teacher"
    def __str__(self):
        return self.personal.__str__()
# ---
class TeacherAchievement(models.Model):
    id = AutoField(primary_key=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)

    class Meta:
        db_table = "teacher_achievement"


