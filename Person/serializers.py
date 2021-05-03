from .models import Health,  Person, Achievement
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'

class HealthSerializer(serializers.ModelSerializer):

    class Meta:
        model = Health
        fields = '__all__'