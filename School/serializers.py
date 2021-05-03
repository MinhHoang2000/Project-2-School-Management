from django.db.models import fields
from rest_framework import serializers

from .models import Classroom

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id']
    
    def validate_class_name(self, value):
        if not Classroom.objects.filter(class_name=value):
                return False
        return True