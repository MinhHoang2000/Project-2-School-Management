from django.http.response import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.views import generic
from django.views.generic.base import TemplateView
# from django.contrib.auth import get_user_model, login, logout, authenticate

from rest_framework import status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
# from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.generics import GenericAPIView

# from .forms import ChangePasswordForm, LoginForm
from .serializers import AccountSerializer, UserLogin, UserChangePassword, RefreshTokenSerializer
from .backend import CustomBackend
# Create your views here.

class Home(TemplateView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Account/Home.html'
    
class Login(APIView):
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'Account/Login.html'

    # permission_classes = [AllowAny]
    # def get(self, request):
    #         form = LoginForm()
    #         return Response({'form':form})

    def post(self, request):
        try :
            serializer = UserLogin(data=request.data)
            if serializer.is_valid():
                user = serializer.validated_data['username']
                user = CustomBackend.authenticate(
                            self,
                            request,
                            username=serializer.validated_data['username'],
                            password=serializer.validated_data['password'],
                            )
                if user == None:
                    #Password not correct but we set message to secure
                    return Response("Username or Password is incorrect !", status=status.HTTP_401_UNAUTHORIZED)
                else :
                    # data = TokenSerializer(user).data
                    refresh = TokenObtainPairSerializer.get_token(user)
                    data = {
                        'id': user.id,
                        'username':user.username,
                        'is_admin':user.is_admin,
                        'refresh_token': str(refresh),
                        'access_token': str(refresh.access_token),
                        'access_expires': int(settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].total_seconds()),
                        'refresh_expires': int(settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'].total_seconds()),
                    }

                    return Response(data, status=status.HTTP_200_OK)
        except  :
            return Response("Account does not exist", status=status.HTTP_401_UNAUTHORIZED)
            
class Logout(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RefreshTokenSerializer
    # def get(self, request):
    #     request.user.auth_token.delete()
    #     return Response("Loggout successfully !", status=status.HTTP_200_OK)
    def post(self, request, *args):
        token = self.get_serializer(data=request.data)
        token.is_valid(raise_exception=True)
        token.save()
        return Response("Logout successfully !",status=status.HTTP_204_NO_CONTENT)

class ChangePassword(APIView):
    permission_classes= [IsAuthenticated,]
    #renderer_classes = [TemplateHTMLRenderer]
    #template_name = 'Account/ChangePassword.html'
    # def get(self, request):
        
    #     form = ChangePasswordForm()
    #     return Response({
    #         'form':form,
    #     })

    def post(self, request):
        pw = UserChangePassword(data = request.data, context={'request': request})
        if pw.is_valid():
            request.user.set_password(pw.validated_data['new_password_2'])
            request.user.save()
        else :
            return JsonResponse({
                'Message':'not valid'
            })
        return JsonResponse({
            'Message':'Change successful'
        })

