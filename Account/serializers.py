from .models import Account
from django.contrib.auth import get_user_model, password_validation
from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from django.utils.text import gettext_lazy as _
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

user = get_user_model()
class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = [
            'username',
            'password',
            'is_admin',
        ]
        extra_kwargs = {'password': {'write_only':True}}
    
    def validate_username(self, value):
        account = Account.objects.filter(username=value)
        if account.exists():
            raise serializers.ValidationError('This username is already taken')
        return value

    def validate_password(self, value):
        try:
            password_validation.validate_password(value)
        except ValidationError:
            raise serializers.ValidationError('Your password is not strong enough')
        return value

# class TokenSerializer(serializers.ModelSerializer):
#     token = serializers.SerializerMethodField()

#     class Meta:
#         model = user
#         fields = ['id', 'username', 'is_admin', 'token']

#     def get_token(self, obj):
#         if Token.objects.filter(user=obj):
#             return Token.objects.get(user=obj).key
#         return Token.objects.create(user=obj).key

# class BearerToken(TokenAuthentication):
#     keyword = "Bearer"

# subclass if you want to use ObtainPairViews in urls.py
# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

#     @classmethod
#     def get_token(cls, user):
#         token = super(MyTokenObtainPairSerializer, cls).get_token(user)

#         # Add custom claims
#         token['username'] = user.username
#         token['id']=user.id
#         token['is_admin']=user.is_admin
#         return token

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
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        
        return attrs
    
    def validate_old_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    
