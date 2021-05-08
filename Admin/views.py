# from Admin.serializers import StudentAchievementSerializer
from Student.utils import get_parent
from functools import partial
from Person.serializers import AchievementSerializer
from Person.models import Achievement
from Student.serializers import StudentParentSerializer, StudentSerializer, StudentAchievementSerializer, ParentSerializer
from Student.models import Student, StudentAchievement, Parent, StudentParent
from Account.serializers import AccountSerializer, AccountDetailSerializer, RegisterSerializer
from Account.models import Account

from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, serializers

# Show list account
class ListAccount(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    # GET -- show list account
    def get(self, request):
        list_account = Account.objects.all()
        accounts_serializer = AccountDetailSerializer(list_account, many = True)
        return Response(accounts_serializer.data, status=status.HTTP_200_OK)

    # POST -- create a account
    def post(self, request):
        info = RegisterSerializer(data=request.data)
        try:
            info.is_valid(raise_exception=True)
            user = Account.objects.create_user(
                username = info.validated_data['username'],
                password = info.validated_data['password'],
                is_admin = info.validated_data['is_admin'],
            ) 
            user.save()
            return Response("Create user successfully ! ",status=status.HTTP_201_CREATED)
        except serializers.ValidationError:
            return Response(info.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountDetail(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    # GET -- show account information
    def get(self, request, account_id):
        try:
            data_account = Account.objects.get(pk=account_id)
            account = AccountDetailSerializer(data_account)
            return Response(account.data, status=status.HTTP_200_OK)
        except Account.DoesNotExist:
            return Response('Account does not exits', status=status.HTTP_400_BAD_REQUEST)

    # DELETE -- delete account
    def delete(self, request, account_id):
        try:
            Account.objects.get(pk=account_id).delete()
            return Response('Delete successfully !', status=status.HTTP_200_OK)
        except Account.DoesNotExist:
            return Response('Account does not exits', status=status.HTTP_400_BAD_REQUEST)

class ListStudent(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    # GET -- show list Student
    def get(self, request):
        list_student = Student.objects.all()
        students_serializer = StudentSerializer(list_student, many=True)
        return Response(students_serializer.data, status=status.HTTP_200_OK)

    # POST -- create Student
    def post(self, request):
        student = StudentSerializer(data=request.data)
        try:
            student.is_valid(raise_exception=True)
            student.save()
            return Response(student.data, status=status.HTTP_201_CREATED)
        except serializers.ValidationError:
            return Response(student.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetail(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    # GET -- show student information 
    def get(self, request, student_id):
        student_check = Student.objects.filter(pk=student_id)
        if student_check :
            data_student = Student.objects.get(pk=student_id)
            student = StudentSerializer(data_student)
            return Response(student.data, status=status.HTTP_200_OK)
        else :
            return Response("Student does not exist !", status=status.HTTP_400_BAD_REQUEST)

    # PUT -- update student information
    def put(self, request, student_id):
        try:
            student = Student.objects.get(pk=student_id)
            student_serializer = StudentSerializer(student, data=request.data, partial=True)
            try: 
                student_serializer.is_valid(raise_exception=True)
                student_serializer.save()
                return Response(student_serializer.data, status=status.HTTP_200_OK)
            except serializers.ValidationError:
                return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Student.DoesNotExist:
            return Response("Student does not exist", status=status.HTTP_400_BAD_REQUEST)
    # Delete -- delete student 
    def delete(self, request, student_id):
        try:
            student = Student.objects.get(pk=student_id)
            student.delete()
            return Response('Delete successfully !', status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response("Student does not exist", status=status.HTTP_400_BAD_REQUEST)
#-----------------------------------------------------ACHIEVEMENT--------------------------------------------
class ListAchievement(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    # GET -- show list achievement
    def get(self, request):
        list_achievement = Achievement.objects.all()
        achievement = AchievementSerializer(list_achievement, many=True)
        return Response(achievement.data, status=status.HTTP_200_OK)
    
    # POST -- create a achievement
    def post(self, request):
        achievement = AchievementSerializer(data=request.data)
        try:
            achievement.is_valid(raise_exception=True)
            achievement.save()
            return Response(achievement.data, status=status.HTTP_201_CREATED)
        except serializers.ValidationError:
            return Response(achievement.errors, status=status.HTTP_400_BAD_REQUEST)

class AchievementDetail(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    # GET -- show achievement detail information
    def get(self, request, achievement_id):
        try:
            achievement = Achievement.objects.get(pk=achievement_id)
            achievement_serializer = AchievementSerializer(achievement)
            return Response(achievement_serializer.data, status=status.HTTP_200_OK)
        except Achievement.DoesNotExist:
            return Response('Achievement does not exist !', status=status.HTTP_400_BAD_REQUEST)
    
    # PUT -- update achievement information
    def put(self, request, achievement_id):
        try:
            achievement = Achievement.objects.get(pk=achievement_id)
            achievement_serializer = AchievementSerializer(achievement, data=request.data, partial=True)
            try:
                achievement_serializer.is_valid(raise_exception=True)
                achievement_serializer.save()
                return Response(achievement_serializer.data, status=status.HTTP_200_OK)
            except serializers.ValidationError:
                return Response(achievement_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Achievement.DoesNotExist:
            return Response('Achievement does not exist !', status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE -- delete achievement
    def delete(self, request, achievement_id):
        try:
            achievement = Achievement.objects.get(pk=achievement_id)
            achievement.delete()
            return Response('Delete successfully !', status=status.HTTP_200_OK)
        except Achievement.DoesNotExist:
            return Response('Achievement does not exist !', status=status.HTTP_400_BAD_REQUEST)

class ListStudentAchievement(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    # GET -- show achievement of student
    def get(self, request, student_pk):
        try:
            student = StudentAchievement.objects.all().filter(student=student_pk)
            student_serializer = StudentAchievementSerializer(student, many=True)
            return Response(student_serializer.data, status=status.HTTP_200_OK)
        except StudentAchievement.DoesNotExist:
            return Response('Not found student_id ', status=status.HTTP_400_BAD_REQUEST)
    
    # POST -- link student with achievement, create a StudentAchievement object
    def post(self, request, student_pk):
        student_achievement = StudentAchievementSerializer(data=request.data)
        try:
            student_achievement.is_valid(raise_exception=True)
            student_achievement.save()
            return Response(student_achievement.data, status=status.HTTP_201_CREATED)
        except serializers.ValidationError:
            return Response(student_achievement.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE -- delete all achievement of student
    def delete(self, request, student_pk):
        try:
            student = StudentAchievement.objects.all().filter(student=student_pk)
            student.delete()
            return Response("Delete successfully", status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response('Not found student_id', status=status.HTTP_400_BAD_REQUEST)
#-------------------------------------------------PARENT----------------------------------------------------------
class ListParent(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    # GET -- show list parent
    def get(self, request):
        list_parent = Parent.objects.all()
        parent_serializer = ParentSerializer(list_parent, many=True)
        try:
            parent_serializer.is_valid(raise_exception=True)
            return Response(parent_serializer.data, status=status.HTTP_200_OK)
        except serializers.ValidationError:
            return Response(parent_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # POST -- create a Parent object
    def post(self, request):
        parent_serializer = ParentSerializer(data=request.data)
        try:
            parent_serializer.is_valid(raise_exception=True)
            parent_serializer.save()
            return Response(parent_serializer.data, status=status.HTTP_201_CREATED)
        except serializers.ValidationError:
            return Response(parent_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ParentDetail(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    # GET -- show parent information
    def get(self, request, parent_id):
        parent = get_parent(parent_id)
        parent_serializer = ParentSerializer(parent)
        try:
            parent_serializer.is_valid(raise_exception=True)
            return Response(parent_serializer.data, status=status.HTTP_200_OK)
        except serializers.ValidationError:
            return Response(parent_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # PUT -- update parent information
    def put(self, request, parent_id):
        parent = get_parent(parent_id)
        parent_serializer = ParentSerializer(parent, data=request.data, partial=True)
        try:
            parent_serializer.is_valid(raise_exception=True)
            return Response(parent_serializer.data, status=status.HTTP_200_OK)
        except serializers.ValidationError:
            return Response(parent_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Delete -- delete parent 
    def delete(self, request, parent_id):
        parent = get_parent(parent_id)
        parent.delete()
        return Response("Delete successfully !", status=status.HTTP_200_OK)

class ListStudentParent(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    # GET -- show list parent of student
    def get(self, request, student_pk):
        try:
          student = StudentParent.objects.all().filter(student=student_pk)
          student_serializer = StudentParentSerializer(student, many=True)
          return Response(student_serializer.data, status=status.HTTP_200_OK)
        except StudentParent.DoesNotExist:
            return Response('Not found student_id ', status=status.HTTP_400_BAD_REQUEST)

    # POST -- link student with parent, create a StudentParent object
    def post(self, request, student_pk):
        student_parent = StudentParentSerializer(data=request.data)
        try:
            student_parent.is_valid(raise_exception=True)
            student_parent.save()
            return Response(student_parent.data, status=status.HTTP_201_CREATED)
        except serializers.ValidationError:
            return Response(student_parent.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE -- delete all parent of student
    def delete(self, request, student_pk):
        try:
            student = StudentParent.objects.all().filter(student=student_pk)
            student.delete()
            return Response("Delete successfully", status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response('Not found student_id', status=status.HTTP_400_BAD_REQUEST)