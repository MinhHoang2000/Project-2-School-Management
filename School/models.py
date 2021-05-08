from django.db import models
import uuid
from Teacher.models import Teacher

# Create your models here.

CHOICES_DAY = [('Mon', 'Monday'),
               ('Tue', 'Tuesday'),
               ('Wed', 'Wednesday'),
               ('Thu', 'Thusday'),
               ('Fri', 'Friday'),
               ('Sat', 'Saturday'),
               ('Sun', 'Sunday')]
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
# Thông tin lớp học
class Classroom(models.Model):
    id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=10)
    location = models.CharField(max_length=10)

    class Meta:
        db_table = "classroom"
# Thong tin mon hoc
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=250)
    GROUP_COURSE = (
        ("Sc", "Science"),
        ("So", "Society"),
        ("Ph", "Physical"),
    )
    group_course = models.CharField(max_length=2, choices = GROUP_COURSE)

    class Meta:
        db_table = "course"
# Thời khóa biểu
class Timetable(models.Model):
    id = models.AutoField(primary_key=True)
    shift = models.CharField(max_length=2, choices=CHOICES_SHIFT)
    day_of_week = models.CharField(max_length=3, choices=CHOICES_DAY)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    class Meta:
        db_table = 'time_table'

# Sổ đầu bài
CLASSIFICATION = (
    ("A", "Tot"),
    ("B", "Kha"),
    ("C", "Trung Binh"),
    ("D", "Yeu")
)
class ClassRecord(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    note = models.TextField()
    student_num = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    classification = models.CharField(max_length=1, choices=CLASSIFICATION)
    shift = models.CharField(max_length=2, choices=CHOICES_SHIFT)
    day_of_week = models.CharField(max_length=3, choices=CHOICES_DAY)
    study_week = models.CharField(max_length=128)

    class Meta:
        db_table = "class_record"

# Thong tin tai lieu hoc tap
class StudyDocument(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    size = models.CharField(max_length=50)
    content_type = models.CharField(max_length=100)
    file_data = models.FileField(upload_to='StudyDocument/%Y/%m/%d/')
    # course = models.ForeignKey(CourseInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = "study_document"