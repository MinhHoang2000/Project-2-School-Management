from django.db.models import fields
from .models import Account
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):


    class Meta:
        model = Account
        fields = [
            'username',
            'password',
        ]
        extra_kwargs = {'password': {'write_only':True}}

class UserLogin(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    is_active = serializers.BooleanField()

class UserChangePassword(serializers.Serializer):
    old_password = serializers.CharField(write_only = True)
    new_password_1 = serializers.CharField(write_only = True)
    new_password_2 = serializers.CharField(write_only = True)

    def validate(self, attrs):
        if attrs['new_password_1'] != attrs['new_password_2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        
        return attrs
    
    def validate_old_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    
