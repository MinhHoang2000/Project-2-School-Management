from Teacher.models import Teacher
from rest_framework import serializers, status
from rest_framework.response import Response
from School.serializers import TeachingInfoSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from School.models import TeachingInfo
from rest_framework.parsers import JSONParser
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import TeacherSerializer
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
        teacher = Teacher.objects.get(account=user)
        return TeachingInfo.objects.filter(teacher=teacher)