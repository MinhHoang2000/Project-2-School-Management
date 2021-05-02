from Account.serializers import AccountSerializer
from Account.models import Account
from rest_framework.views import APIView

from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, serializers

# Create your views here.

class Register(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

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