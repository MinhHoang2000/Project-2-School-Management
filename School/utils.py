from .models import ClassRecord, Classroom, Course
from rest_framework import exceptions

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