# from Admin.serializers import StudentAchievementSerializer
from Teacher.serializers import StudentInfoSerializer, TeacherSerializer
from django.db import models
from Account.models import Account
from Person.utils import create_person, create_health
from django.db.models import fields
from Student.models import Grade, Parent, Student, StudentAchievement, StudentParent
from Person.serializers import PersonSerializer, AchievementSerializer, HealthSerializer
from Account.serializers import AccountSerializer
from School.serializers import ClassroomSerializer, CourseSerializer
from Person.utils import update_person, update_health

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
    # parent_id  = serializers.PrimaryKeyRelatedField(source = 'parent', read_only = True, many = True)
    class Meta:
        model = Student
        fields = ['id', 'account', 'personal', 'status', 'classroom_id' ,'admission_year', 'health']

    def create(self, validated_data):
        # logger.error(validated_data)
        # name = validated_data['personal']['first_name'] + validated_data['personal']['last_name'] + str(random.randint(1000, 9999))
        person = create_person(validated_data.pop('personal'))
        data_account = validated_data.pop('account')
        account = Account.objects.create_user(
            username = data_account['username'],
            password = data_account['password'],
        )
        account.save()
        try :
            if validated_data['health'] == None :
                    student = Student.objects.create(
                    account = account,
                    personal = person,
                    **validated_data
                )
            else:
                health = create_health(validated_data.pop('health'))
                logger.error(validated_data)
                student = Student.objects.create(
                    account = account,
                    personal = person,
                    health = health,
                    **validated_data
                )
        except Exception:
            raise serializers.ValidationError('Something wrong with your student information')
        student.save()
        return student
    
    def update(self, instance ,validated_data):
        try :
            account = AccountSerializer(instance=instance.account, data=validated_data.pop('account'), partial=True)
            account.is_valid(raise_exception=True)
            account.save()
        except KeyError:
            pass

        try :
            update_person(instance.personal, validated_data.pop('personal'))
        except KeyError:
            pass

        try :
            if instance.health is None:
                health = create_health(validated_data.pop('health'))
                instance.health = health
            else:
                update_health(instance.health, validated_data.pop('health'))
        except KeyError:
            pass
        instance.classroom_id = validated_data.get('classroom_id', instance.classroom_id)
        instance.status = validated_data.get('status', instance.status)
        instance.admission_year = validated_data.get('admission_year', instance.admission_year)
        instance.save()
        return instance

class StudentAchievementSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StudentAchievement
        fields = '__all__'
    
    def create(self, validated_data):
        student_achievement = StudentAchievement.objects.create(
            student=validated_data['student'],
            achievement=validated_data['achievement']
        )
        student_achievement.save()
        return student_achievement

class ParentSerializer(serializers.ModelSerializer):
    personal = PersonSerializer()
    class Meta:
        model = Parent
        fields = '__all__'

    def create(self, validated_data):
        personal = create_person(validated_data.pop('personal'))
        parent = Parent.objects.create(
            father_or_mother = validated_data['father_or_mother'],
            job = validated_data['job'],
            personal = personal
        )
        parent.save()
        return parent

class StudentParentSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentParent
        fields = '__all__'

        def create(self, validated_data):
            student_parent = StudentParent.objects.create(
                student = validated_data['student'],
                parent = validated_data['parent']
            )
            student_parent.save()
            return student_parent

class GradeSerializer(serializers.ModelSerializer):

    course = CourseSerializer(required = False)
    student = StudentInfoSerializer(required = False)
    teacher = TeacherSerializer(required = False)
    school_year = serializers.CharField(required = False ,allow_null = True)
    test_p = serializers.FloatField(required = False ,allow_null = True)
    mid_term_p = serializers.FloatField(required = False ,allow_null = True)
    term_p = serializers.FloatField(required = False ,allow_null = True)
    final_term_p = serializers.FloatField(required = False ,allow_null = True)

    class Meta:
        model = Grade
        fields = ['id', 'course', 'student', 'teacher', 'school_year', 'semester' ,'test_p', 'mid_term_p', 'term_p', 'final_term_p']

    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        
        instance.test_p = validated_data.get('test_p', instance.test_p)
        instance.mid_term_p = validated_data.get('mid_term_p', instance.mid_term_p)
        instance.term_p = validated_data.get('term_p', instance.term_p)
        instance.final_term_p = validated_data.get('final_term_p', instance.final_term_p)
        instance.save()
        return instance