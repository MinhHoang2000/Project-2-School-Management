from django.db import models
import uuid
# Create your models here.

CHOICES_SHIFT = (
        ("M1", "7:15-8:00"),
        ("M2", "8:10-8:55"),
        ("M3", "9:05-9:50"),
        ("M4", "10:05-10:50"),
        ("M5", "11:00-11:45"),
        ("A1", "13:00-13:45"),
        ("A2", "13:55-14:10"),
        ("A3", "14:50-15:35"),
        ("A4", "15:50-16:35"),
        ("A5", "16:45-17:30"),
    )
CHOICES_DAY = (
        ("2", "Thứ 2"),
        ("3", "Thứ 3"),
        ("4", "Thứ 4"),
        ("5", "Thứ 5"),
        ("6", "Thứ 6"),
        ("7", "Thứ 7"),
    )
# Thong tin thiet bi
class DeviceInfo(models.Model):
    id = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4, primary_key=True)
    device_name = models.CharField(max_length=250)
    DEVICE_STATUS = (
        ("N", "Normal"),
        ("B", "Broken"),
        ("BB", "Be Borrowed")
    )
    device_status = models.CharField(max_length=2, choices=DEVICE_STATUS)

    class Meta:
        db_table = "device"

class DeviceMan(models.Model):
    id = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4, primary_key=True)
    device = models.ForeignKey(DeviceInfo, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=3, choices=CHOICES_DAY )
    shift = models.CharField(max_length=2, choices=CHOICES_SHIFT)

    class Meta:
        db_table = 'device_manage'