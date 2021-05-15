from School.models import Classroom
from Person.serializers import HealthSerializer, PersonSerializer
from Student.models import Student
from django.db.models import fields
from Teacher.models import Teacher
from rest_framework import serializers

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'

class StudentInfoSerializer(serializers.ModelSerializer):
    personal = PersonSerializer()

    class Meta:
        model = Student
        fields = ['id', 'personal', ]


