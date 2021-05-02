

from django.db.models.fields import CharField
from rest_framework.serializers import ValidationError
from rest_framework import serializers

from django.contrib.auth import get_user_model, password_validation

from Account.models import Account

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    is_admin = serializers.BooleanField()

    def validate_username(self, value):
        account = Account.objects.filter(username=value)
        if account.exists():
            raise serializers.ValidationError({'Message': 'This username is already taken'})
        return value

    def validate_password(self, value):
        try:
            password_validation.validate_password(value)
        except ValidationError:
            raise serializers.ValidationError({'Message' :'Password must have characters and numbers !'})
        return value

class DeleteSerializer(serializers.Serializer):
    username = serializers.CharField()

    def validate_username(self, value):
        account = Account.objects.filter(username=value)
        if not account.exists():
            raise serializers.ValidationError({'Message': 'This username does not exist ! '})
        return value
