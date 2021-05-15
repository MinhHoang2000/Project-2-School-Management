from django.urls import path, re_path
from .views import ListGrade, ListStudent, ListTeachingInfo

urlpatterns = [
    path('me/teaching-info', ListTeachingInfo.as_view(), name='teaching_information'),
    path('list-student/class/<int:classroom_id>', ListStudent.as_view(), name='list_student_of_class'),
    path('list-student-grade/class/<int:classroom_id>', ListGrade.as_view(), name='list_student_grade_of_class'),
]