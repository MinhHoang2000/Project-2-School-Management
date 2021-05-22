
from django.contrib.auth.models import AnonymousUser
from rest_framework import exceptions
from .models import Teacher

def get_current_teacher(account):
    if account is AnonymousUser:
        return exceptions.NotAuthenticated("You need login")
    try: 
        teacher = Teacher.objects.get(account=account)
        return teacher
    except Teacher.DoesNotExist:
        return exceptions.NotFound("Not found teacher")

