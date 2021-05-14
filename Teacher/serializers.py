from django.db.models import fields
from Teacher.models import Teacher
from rest_framework import serializers

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'