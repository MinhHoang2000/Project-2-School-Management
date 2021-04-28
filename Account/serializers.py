from .models import Account
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):


    class Meta:
        model = Account
        fields = [
            'username',
            'password',
        ]
        extra_kwargs = {'password': {'write_only':True}}

class UserLogin(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    is_active = serializers.BooleanField()
