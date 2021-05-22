from School.utils import get_classrecord
from Student.utils import get_student
from Teacher.utils import get_current_teacher
from Student.serializers import GradeSerializer, StudentSerializer
from School.serializers import ClassRecordSerializer, TeachingInfoSerializer
from Student.models import Grade, Student
from Teacher.models import Teacher
from School.models import ClassRecord, Classroom, Course, TeachingInfo
from .serializers import StudentInfoSerializer, TeacherSerializer

from rest_framework import exceptions
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework import generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

# Show class, course , ... which current teacher teaches
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

# Show list of students in a class
class ListStudent(generics.ListAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentInfoSerializer
    filter_backends = (DjangoFilterBackend,)
    
    def get_queryset(self):
        try:
           classroom = Classroom.objects.get(pk=self.kwargs['classroom_id'])
           student = Student.objects.all().filter(classroom=classroom).order_by(
               'personal__last_name', 'personal__first_name', 'personal__date_of_birth')
           return student
        except Classroom.DoesNotExist:
            return exceptions.NotFound('Class does not exist')

# Show list of student's grade of a course in a class
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

# Grade Detail
class GradeDetail(APIView):

    # GET -- Show grade of a student of a course in a class
    def get(self, request, grade_id):
        user = self.request.user
        try:
            teacher = Teacher.objects.get(account=user)
            try:
                grade = Grade.objects.get(pk=grade_id, teacher=teacher)
                grade_serializer = GradeSerializer(grade)
                return Response(grade_serializer.data, status=status.HTTP_200_OK)
            except Grade.DoesNotExist:
                Response("Not found grade", status=status.HTTP_400_BAD_REQUEST)
        except Teacher.DoesNotExist:
            return Response('Teacher does not exist', status=status.HTTP_400_BAD_REQUEST)
    # PUT -- update grade
    def put(self, request, grade_id):
        user = self.request.user
        try:
            teacher = Teacher.objects.get(account=user)
            try:
                grade = Grade.objects.get(pk=grade_id, teacher=teacher)
                grade_serializer = GradeSerializer(grade, data=request.data, partial=True)
                try:
                    grade_serializer.is_valid(raise_exception=True)
                    grade_serializer.save()
                    return Response(grade_serializer.data, status=status.HTTP_200_OK)
                except serializers.ValidationError:
                    return Response(grade_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Grade.DoesNotExist:
                Response("Not found grade", status=status.HTTP_400_BAD_REQUEST)
        except Teacher.DoesNotExist:
            return Response('Teacher does not exist', status=status.HTTP_400_BAD_REQUEST)
    

# Show grade of all courses of a student
class AllGradeStudent(generics.ListAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('school_year', 'semester', )

    def get_queryset(self):
        student_id = self.kwargs['student_id']
        student = get_student(student_id)
        try:
            grade_student = Grade.objects.all().filter(student=student).order_by(
                'student__personal__last_name', 
                'student__personal__first_name', 
                'student__personal__date_of_birth' )
            return grade_student
        except Grade.DoesNotExist:
            return exceptions.NotFound('Grade of student does not exist')

# Show list classrecord
class ListClassRecord(generics.ListAPIView):
    queryset = ClassRecord.objects.all()
    serializer_class = ClassRecordSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'day_of_week', 'study_week', 'classroom_id', 'course_id', 'school_year', 'semester')

    def get_queryset(self):
        user = self.request.user
        try:
            teacher = Teacher.objects.get(account=user)
            classrecord = ClassRecord.objects.all().order_by(
                 'school_year', 'semester', 'study_week', 'day_of_week', 'classroom__class_name'
            )
            return classrecord
        except Teacher.DoesNotExist:
            return exceptions.NotFound('Teacher does not exist')

# 
class ClassRecordDetail(APIView):

    def get(self, request, classrecord_id):
        classrecord = get_classrecord(classrecord_id)
        classrecord_serializer = ClassRecordSerializer(classrecord)
        return Response(classrecord_serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, classrecord_id):
        user = self.request.user
        teacher = get_current_teacher(user)
        try:
            classrecord = ClassRecord.objects.get(pk=classrecord_id, teacher=teacher)
            classrecord_serializer = ClassRecordSerializer(classrecord, data=request.data, partial = True)
            try:
                classrecord_serializer.is_valid(raise_exception=True)
                classrecord_serializer.save()
                return Response(classrecord_serializer.data, status=status.HTTP_200_OK)
            except serializers.ValidationError:
                return Response(classrecord_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except ClassRecord.DoesNotExist:
            return Response('Not found classrecord_id or you do not have permission', status=status.HTTP_400_BAD_REQUEST)
# --
class ClassRecordCreate(APIView):
    def post(self, request):
        classrecord_serializer = ClassRecordSerializer(data=request.data)
        try:
            classrecord_serializer.is_valid(raise_exception=True)
            classrecord_serializer.save()
            return Response(classrecord_serializer.data, status=status.HTTP_201_CREATED)
        except serializers.ValidationError:
            return Response(classrecord_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            