from Account.serializers import AccountSerializer
from Account.models import Account
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status, serializers, exceptions

from django.contrib.auth import get_user_model

from Account.utils import create_account, update_account
from .forms import RegisterForm
# Create your views here.

class Register(APIView):
    permission_classes = (IsAuthenticated,IsAdminUser)
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'Admin/Register.html'
    # def get(self, request):
    #     form = RegisterForm()
    #     return Response({
    #         'form':form
    #     })
    
    def post(self, request):
        info = AccountSerializer(data=request.data, context={'request':request})
        try:
            info.is_valid(raise_exception=True)
            user = Account.objects.create_user(
                username = info.validated_data['username'],
                password = info.validated_data['password'],
                is_admin = info.validated_data['is_admin'],
            ) 
            user.save()
        except serializers.ValidationError:
            return Response(info.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Create user successfully ! ",status=status.HTTP_201_CREATED)