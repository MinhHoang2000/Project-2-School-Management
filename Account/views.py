from django.conf import settings

from rest_framework import serializers, status, generics
from rest_framework.views import APIView
# from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.generics import GenericAPIView

from .serializers import AccountSerializer, UserChangePassword, RefreshTokenSerializer
from .backends import CustomBackend

from Account.serializers import AccountSerializer, AccountDetailSerializer, RegisterSerializer
from Account.models import Account

# Create your views here.

class Login(APIView):
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['username']
            user = CustomBackend.authenticate(
                        self,
                        request,
                        username=serializer.validated_data['username'],
                        password=serializer.validated_data['password'],
                        )
            if user == None:
                #Password not correct but we set this message to secure
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
        except serializers.ValidationError:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
            
class Logout(GenericAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = RefreshTokenSerializer
    def post(self, request, *args):
        token = self.get_serializer(data=request.data)
        token.is_valid(raise_exception=True)
        token.save()
        return Response("Logout successfully !",status=status.HTTP_204_NO_CONTENT)

class ChangePassword(APIView):
    permission_classes= [IsAuthenticated,]
    def put(self, request):
        password = UserChangePassword(data = request.data, context={'request': request})
        try:
            password.is_valid(raise_exception=True)
            request.user.set_password(password.validated_data['new_password_2'])
            request.user.save()
        except serializers.ValidationError:
            return Response(password.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Change password successfully !", status=status.HTTP_200_OK)

