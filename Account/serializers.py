from .models import Account

from django.contrib.auth import get_user_model, password_validation
from django.utils.text import gettext_lazy as _

from rest_framework import serializers
from rest_framework.serializers import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

import re
#-------------------------------------------------------------------------------------------------------------------#
def check_username(value):
    string_check= re.compile('[@_!#$%^&*()<>?/\|}{~: ]')
    if string_check.search(value) != None:
        raise serializers.ValidationError({"Message":"Username contains only characters or numbers"})
# use for Account app
user = get_user_model()
class AccountSerializer(serializers.Serializer):
    username = serializers.CharField(validators=[check_username])
    password = serializers.CharField()
    is_admin = serializers.BooleanField(required=False)
    
    def create(self, validated_data):
        if self.context.get('is_admin', False):
            return user.objects.create_superuser(**validated_data)
        return user.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        try:
            password = validated_data.pop('password')
            instance.set_password(password)
        except KeyError:
            pass

        instance.save()
        return instance

class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token': _('Token is invalid or expired')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')

class UserChangePassword(serializers.Serializer):
    old_password = serializers.CharField(write_only = True)
    new_password_1 = serializers.CharField(write_only = True, validators=[password_validation.validate_password])
    new_password_2 = serializers.CharField(write_only = True, validators=[password_validation.validate_password])

    def validate(self, attrs):
        if attrs['new_password_1'] != attrs['new_password_2']:
            raise serializers.ValidationError({"Message":"Password fields didn't match !"})
        return attrs
    
    def validate_old_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError({"Message":"Old password is not correct !"})
        return value

# Use for Admin app 
class AccountDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'

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