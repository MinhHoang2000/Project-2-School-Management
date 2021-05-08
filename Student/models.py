from django.db import models
from Person.models import  Person, Achievement, Health
from School.models import  Classroom, Course
from Account.models import Account
import  uuid

# Thông tin học sinh
class Student(models.Model):
    id = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4, primary_key=True, editable=False)
    personal = models.OneToOneField(Person, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, null=True)
    # achievement = models.ManyToManyField(Achievement)
    health = models.OneToOneField(Health, on_delete=models.CASCADE, null=True)
    admission_year = models.DateField(default="14-7-2015")
    account = models.OneToOneField(Account, on_delete=models.CASCADE, null=True)
    STUDENT_STATUS = (
        ("L", "Learing"),
        ("O", "Out"),
        ("D", "Done"),
        ("F1", "Fail 1 year"),
        ("F2", "Fail 2 years"),
    )
    status = models.CharField(max_length=2, choices=STUDENT_STATUS, default="L")

    class Meta:
        db_table = "student"

    def __str__(self):
        return self.personal.__str__()

# Thông tin phụ huynh học sinh
class Parent(models.Model):
    id = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid3, primary_key=True)
    CHOICES_PARENT = (
        ("F", "Father"),
        ("M", "Mother"),
    )
    father_or_mother = models.CharField(max_length=1, choices=CHOICES_PARENT)
    job = models.CharField(max_length=250)
    personal = models.OneToOneField(Person, on_delete=models.CASCADE)
    # student = models.ManyToManyField(Student, related_name='parent')

    class Meta:
        db_table = "parent"

    def __str__(self):
        return self.personal.__str__()
#--------
class StudentAchievement(models.Model):
    id = models.AutoField(primary_key=True)
    student= models.ForeignKey(Student, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)

    class Meta:
        db_table = "student_achievement"
class StudentParent(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    class Meta:
        db_table = "student_parent"
#-------
# Điểm học sinh
class Score(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    school_year = models.CharField(max_length=250)
    test_p = models.FloatField()
    mid_term_p = models.FloatField()
    term_p = models.FloatField()
    final_term_p = models.FloatField()

    class Meta:
        db_table = "score"
# Điểm hạnh kiểm
class Conduct(models.Model):
    SCORES = [('T', 'Tot'),
              ('K', 'Kha'),
              ('TB', 'Trung binh'),
              ('Y', 'Yeu')]
    id = models.AutoField(primary_key=True)
    score = models.CharField(max_length=2, choices=SCORES)
    term = models.SmallIntegerField()
    school_year = models.CharField(max_length=250)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        db_table = 'conduct'