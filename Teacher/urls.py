from django.urls import path, re_path
from .views import AllGradeStudent, ClassRecordCreate, ClassRecordDetail, ListClassRecord, ListGrade, ListStudent, ListTeachingInfo, GradeDetail

urlpatterns = [
    path('me/teaching-info', ListTeachingInfo.as_view(), name='teaching_information'),
    path('list-student/class/<int:classroom_id>', ListStudent.as_view(), name='list_student_of_class'),
    path('list-student-grade/class/<int:classroom_id>', ListGrade.as_view(), name='list_student_grade_of_class'),

    path('grade/<int:grade_id>', GradeDetail.as_view(), name='grade_detail'),
    path('grade/student/<slug:student_id>', AllGradeStudent.as_view(), name='all_grade_of_student'),

    path('list-classrecord', ListClassRecord.as_view(), name='list_classrecord'),
    path('classrecord/<int:classrecord_id>', ClassRecordDetail.as_view(), name='classrecord_detail'),
    path('classrecord/create', ClassRecordCreate.as_view(), name='create_classrecord'),
]