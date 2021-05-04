from rest_framework.serializers import ValidationError
from rest_framework import serializers

from django.contrib.auth import get_user_model, password_validation

from Account.models import Account

import re

def check_username(value):
    string_check= re.compile('[@_!#$%^&*()<>?/\|}{~: ]')
    if string_check.search(value) != None:
        raise serializers.ValidationError({"Message":"Username contains only characters or numbers"})

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(validators=[check_username])
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
            raise serializers.ValidationError({'Message' :'Password must have characters, numbers and length >= 8'})
        return value

class DeleteSerializer(serializers.Serializer):
    username = serializers.CharField()

    def validate_username(self, value):
        account = Account.objects.filter(username=value)
        if not account.exists():
            raise serializers.ValidationError({'Message': 'This username does not exist ! '})
        return value
