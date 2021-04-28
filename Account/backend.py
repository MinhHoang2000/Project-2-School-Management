from django.contrib.auth.backends import BaseBackend
from django.http.response import JsonResponse
from .models import Account
from rest_framework import authentication, exceptions
from django.conf import settings
import jwt

class CustomBackend(BaseBackend):
    def authenticate(self, request, **kwargs):
        username = kwargs['username'];
        password = kwargs['password']

        try:
            user = Account.objects.get(username=username)
            if user.check_password(password):
                return user
            else:
                return None
        except Account.DoesNotExist:
            return JsonResponse({
                'Message':"Can't find username"
            })

    def get_user(self, user_id):
        try:
            return Account.objects.get(pk=user_id)
        except Account.DoesNotExist:
            return None
    
    def get_user_permissions(self, user_obj, obj=None):
        if not user_obj.is_active or user_obj.is_anonymous:
            return set()

        perms = user_obj.permissions.all().value_list()
        perms = ["{code}" for id, name, code in perms]

        return perms
class JWTAuthentication(authentication.TokenAuthentication):
    def jwtauthenticate(self, request):
        auth_data = authentication.get_authorization_header(request)
        if not auth_data:
            return None
        prefix, token = auth_data.decode('utf-8').split(' ')
        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms="HS256")
            user = Account.objects.get(username=payload['username'])
            return (user, token)

        except jwt.DecodeError as identifier:
            return False
        except jwt.ExpiredSignatureError as identifier:
            return False
       