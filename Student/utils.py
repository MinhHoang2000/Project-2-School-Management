from Student.models import Student, Parent, StudentAchievement, Score
from rest_framework import exceptions

def get_student(student_id):
    try:
        student = Student.objects.get(pk=student_id)
        return student
    except Student.DoesNotExist:
        raise exceptions.NotFound('Student does not exist')

def get_parent(parent_id):
    try:
        parent = Parent.objects.get(pk=parent_id)
        return parent
    except Parent.DoesNotExist:
        raise exceptions.NotFound('Parent does not exist')


# def get_score(student):
#     try:
#         return Score.objects.get(pk=pk)
#     except Score.DoesNotExist:
#         raise exceptions.NotFound('Grade does not exist')