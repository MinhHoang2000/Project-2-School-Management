from django.db.models import fields
from rest_framework import serializers

from .models import Classroom, Course, TeachingInfo

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id']
    
    def validate_class_name(self, value):
        if not Classroom.objects.filter(class_name=value):
                return False
        return True

class TeachingInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeachingInfo
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'