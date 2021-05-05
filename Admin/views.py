from Student.serializers import StudentSerializer
from Student.models import Student
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
        except serializers.ValidationError:
            return Response(info.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Create user successfully ! ",status=status.HTTP_201_CREATED)

class AccountDetail(APIView):
    # GET -- show account information
    def get(self, request, account_id):
        if Account.objects.filter(pk=account_id):
            data_account = Account.objects.get(pk=account_id)
            account = AccountDetailSerializer(data_account)
            return Response(account.data, status=status.HTTP_200_OK)
        else:
            return Response('Account does not exits', status=status.HTTP_400_BAD_REQUEST)
    # DELETE -- delete account
    def delete(self, request, account_id):
        if Account.objects.filter(pk=account_id):
            Account.objects.get(pk=account_id).delete()
            return Response('Delete successfully !', status=status.HTTP_200_OK)
        else:
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
    # GET -- show student information 
    def get(self, request, student_id):
        student_check = Student.objects.filter(pk=student_id)
        if student_check :
            data_student = Student.objects.get(pk=student_id)
            student = StudentSerializer(data_student)
            return Response(student.data, status=status.HTTP_200_OK)
        else :
            return Response("Student does not exist !", status=status.HTTP_400_BAD_REQUEST)