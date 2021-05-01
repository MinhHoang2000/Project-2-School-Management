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
    permission_classes = (IsAuthenticated,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Admin/Register.html'
    def get(self, request):
        form = RegisterForm()
        return Response({
            'form':form
        })
    
    def post(self, request):
        # if request.data.is_admin :        
            try:
                create_account(request.data, is_admin=True)
            except serializers.ValidationError:
                return JsonResponse({
                    'Message':'Create superuser Error'
                })
        # else :
            # try:
            #     create_account(request.data, is_admin=False)
            # except serializers.ValidationError:
            #     return JsonResponse({
            #         'Message':'Create user Error'
            #     })
            return JsonResponse({
                "Message":"Create successful",
                "username":request.data.username,
            })  