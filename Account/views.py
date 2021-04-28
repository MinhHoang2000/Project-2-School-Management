from django.http.response import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.views.generic.base import TemplateView
from django.contrib.auth import login, logout

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.authtoken.models import Token

from .forms import LoginForm
from .serializers import AccountSerializer, UserLogin
from .backend import CustomBackend, JWTAuthentication
# Create your views here.

class Home(TemplateView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Account/Home.html'
    
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
                if user.is_active:
                    login(request, user)
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
            # CookieResponse = HttpResponse("Cookie Set")
            # CookieResponse.set_cookie('token', token.key)
            # CookieResponse.set_cookie('username', user.username)
            # return JsonResponse(data)
            #Response.set_cookie('token', token.key, max_age=3600)
            return HttpResponseRedirect(request.GET.get('next', settings.LOGIN_REDIRECT_URL))
            # return Response(data, status=status.HTTP_200_OK)
        else:
             return Response({
            'error_messages': serializer.errors,
            'error_code': 400
        }, status=status.HTTP_400_BAD_REQUEST)

class Logout(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        #user = request.user.auth_token.delete()
        logout(request)

        return HttpResponse("<h1>You logout</h1>")
