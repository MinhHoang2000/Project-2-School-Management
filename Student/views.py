from Student.serializers import StudentSerializer, StudentAchievementSerializer
from Student.models import Student, StudentAchievement

from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, serializers
# Create your views here.

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
class ListStudentAchievement(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    # GET -- show achievement of student
    def get(self, request, student_pk):
        try:
            student = StudentAchievement.objects.all().filter(student=student_pk)
            student_serializer = StudentAchievementSerializer(student, many=True)
            return Response(student_serializer.data, status=status.HTTP_200_OK)
        except StudentAchievement.DoesNotExist:
            return Response('Student does not exist ', status=status.HTTP_400_BAD_REQUEST)
    
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
            return Response('Error', status=status.HTTP_400_BAD_REQUEST)