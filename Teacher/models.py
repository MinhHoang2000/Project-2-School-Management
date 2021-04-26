from django.db import models
import uuid
from Person.models import Person, Achievement
from Account.models import Account

# Create your models here.
# Thông tin giáo viên
class Teacher(models.Model):
    id = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4, primary_key=True)
    personal = models.OneToOneField(Person, on_delete=models.CASCADE)
    achievement = models.ManyToManyField(Achievement)
    account = models.OneToOneField(Account, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "teacher"
    def __str__(self):
        return self.personal.__str__()
