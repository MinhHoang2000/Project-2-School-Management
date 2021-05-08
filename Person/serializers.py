from .models import Health,  Person, Achievement
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class AchievementSerializer(serializers.ModelSerializer):
    achievement_name = serializers.CharField()
    created_at = serializers.DateField(required=False, allow_null = True)
    class Meta:
        model = Achievement
        fields = '__all__'
    
    def create(self, validated_data):
        achievement = Achievement.objects.create(
            achievement_name = validated_data['achievement_name'],
            created_at = validated_data['created_at'],
        )
        achievement.save()
        return achievement
    
    def update(self, instance, validated_data):
        instance.achievement_name = validated_data.get('achievement_name', instance.achievement_name)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.save()
        return instance

class HealthSerializer(serializers.ModelSerializer):

    class Meta:
        model = Health
        fields = '__all__'