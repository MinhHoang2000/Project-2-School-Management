from Account.models import Account
from Person.utils import create_person, create_health
from django.db.models import fields
from Student.models import Student
from Person.serializers import PersonSerializer, AchievementSerializer, HealthSerializer
from Account.serializers import AccountSerializer
from School.serializers import ClassroomSerializer

from rest_framework import serializers

import string
import random

import logging
logger = logging.getLogger(__name__)

def random_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class StudentSerializer(serializers.ModelSerializer):
    
    account = AccountSerializer(required = False)
    personal = PersonSerializer()
    health = HealthSerializer(required = False ,allow_null = True)
    classroom_id = serializers.CharField()
    parent_id  = serializers.PrimaryKeyRelatedField(source= 'parent', read_only = True, many = True)

    class Meta:
        model = Student
        fields = ['id', 'account', 'personal', 'status', 'classroom_id' ,'admission_year', 'health', 'parent_id']

    def create(self, validated_data):
        logger.error(validated_data)
        # name = validated_data['personal']['first_name'] + validated_data['personal']['last_name'] + str(random.randint(1000, 9999))
        person = create_person(validated_data.pop('personal'))
        data_account = validated_data.pop('account')
        account = Account.objects.create_user(
            username = data_account['username'],
            password = data_account['password'],
        )
        account.save()
        try :
            student = Student.objects.create(
                account = account,
                personal = person,
                **validated_data
            )
        except Exception:
            raise serializers.ValidationError('Something wrong with your student information')
        
        # if 'health' in validated_data :
        #     create_health(validated_data.pop('health'))
        student.save()

        return student
