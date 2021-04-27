from django.http.response import JsonResponse
from django.shortcuts import render
from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from .models import Account
from .forms import LoginForm
from .serializers import AccountSerializer, UserLogin
from .backend import CustomBackend
# Create your views here.

class Login(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Account/Login.html'

    permission_classes = [AllowAny]
    def get(self, request):
        
       form = LoginForm()
       return Response({'form':form})

    def post(self, request):
        serializer = UserLogin(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['username']
            user = CustomBackend.authenticate(
                        self,
                        request,
                        username=serializer.validated_data['username'],
                        password=serializer.validated_data['password'],
                        )
            if user:
                    token, created = Token.objects.get_or_create(user=user)
            else:
                return Response({
                        'error_message':'Username or Password is incorrect !',
                        'error_code':400
                }, status=status.HTTP_200_OK)
            data = {
                    'token': token.key,
                    'user_id': user.id,
                    'username': user.username
            }
            return JsonResponse(data)
        else:
             return Response({
            'error_messages': serializer.errors,
            'error_code': 400
        }, status=status.HTTP_400_BAD_REQUEST)
