from .models import Account
from django.contrib.auth import get_user_model, password_validation
from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from django.utils.text import gettext_lazy as _
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

#-------------------------------------------------------------------------------------------------------------------#

user = get_user_model()
class AccountSerializer(serializers.Serializer):
    id = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()

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

class UserLogin(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserChangePassword(serializers.Serializer):
    old_password = serializers.CharField(write_only = True)
    new_password_1 = serializers.CharField(write_only = True)
    new_password_2 = serializers.CharField(write_only = True)

    def validate(self, attrs):
        if attrs['new_password_1'] != attrs['new_password_2']:
            raise serializers.ValidationError({"Message":"Password fields didn't match !"})
        
        return attrs
    
    def validate_old_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError({"Message":"Old password is not correct !"})
        return value

    
