from django.conf import settings
from .models import ClassRecord, Classroom, Course, StudyDocument
from rest_framework import exceptions
import os
from rest_framework import serializers

def get_classrecord(classrecord_id):
    try:
        classrecord = ClassRecord.objects.get(pk=classrecord_id)
        return classrecord
    except exceptions:
        return exceptions.NotFound("Not found classrecord")

def get_classroom(classroom_id):
    try:
        classroom = Classroom.objects.get(pk=classroom_id)
        return classroom
    except exceptions:
        return exceptions.NotFound("Not found classroom")

def get_course(course_id):
    try:
        course = Course.objects.get(pk=course_id)
        return course
    except exceptions:
        return exceptions.NotFound("Not found course")

def get_studydocument(file_id):
    try:
        study_document = StudyDocument.objects.get(pk=file_id)
        return study_document
    except StudyDocument.DoesNotExist:
        raise exceptions.NotFound("Not found file")

# def delete_studydocument(file_id):
#     study_document = get_studydocument(file_id)
#     return study_document.delete()