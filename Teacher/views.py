from Student.serializers import GradeSerializer, StudentSerializer
from Student.models import Grade, Student
from rest_framework import exceptions
from Teacher.models import Teacher
from rest_framework import serializers, status
from rest_framework.response import Response
from School.serializers import TeachingInfoSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from School.models import Classroom, TeachingInfo
from rest_framework.parsers import JSONParser
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import StudentInfoSerializer, TeacherSerializer
# Create your views here.

# class ListTeachingInfo(APIView):

#     def get(self, request):
#         if request.data['teacher_id'] is None :
#             return Response("Not found teacher_id", status=status.HTTP_400_BAD_REQUEST)
#         teacher_id = request.data['teacher_id']
#         teacher = get_teacher(teacher_id)
#         teaching_info = TeachingInfo.objects.all().filter(teacher=teacher_id)
#         teaching_info_serializer = TeachingInfoSerializer(teaching_info, many=True)
#         return Response(teaching_info_serializer.data, status=status.HTTP_200_OK)

class ListTeachingInfo(generics.ListAPIView):
    
    queryset = TeachingInfo.objects.all()
    serializer_class = TeachingInfoSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('classroom', 'course', )

    def get_queryset(self):
        user = self.request.user
        try:
            teacher = Teacher.objects.get(account=user)
            try:
                teching_info_list = TeachingInfo.objects.filter(teacher=teacher)
                return teching_info_list
            except TeachingInfo.DoesNotExist:
                return exceptions.NotFound('Teacher does not have teaching information')
        except Teacher.DoesNotExist:
            return exceptions.NotFound('Teacher does not exist')

class ListStudent(generics.ListAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentInfoSerializer
    filter_backends = (DjangoFilterBackend,)
    
    def get_queryset(self):
        try:
           classroom = Classroom.objects.get(pk=self.kwargs['classroom_id'])
           student = Student.objects.all().filter(classroom=classroom).order_by('personal__last_name', 'personal__first_name', 'personal__date_of_birth')
           return student
        except Classroom.DoesNotExist:
            return exceptions.NotFound('Class does not exist')

class ListGrade(generics.ListAPIView):

    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('course', 'school_year', 'semester')

    def get_queryset(self):
        user = self.request.user
        try:
            teacher = Teacher.objects.get(account=user)
            try:
                classroom = Classroom.objects.get(pk=self.kwargs['classroom_id'])
                students = Student.objects.all().filter(classroom=classroom)
                student_grade = Grade.objects.all().filter(student__in= students, teacher=teacher).order_by(
                    'student__personal__last_name', 
                    'student__personal__first_name', 
                    'student__personal__date_of_birth' )
                return student_grade
            except Classroom.DoesNotExist:
                return exceptions.NotFound('Class does not exist')
        except Teacher.DoesNotExist:
            return exceptions.NotFound('Teacher does not exist')

        

