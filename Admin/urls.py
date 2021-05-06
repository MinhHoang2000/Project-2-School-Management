from django.urls import path
from .views import AccountDetail, ListAccount, ListStudent, StudentDetail

urlpatterns= [

    # account management
    # path('register', Register.as_view(), name='register'),
    # path('delete', Delete.as_view(), name='delete'),

    # account list
    path('accounts',ListAccount.as_view(), name='list_account'),
    path('accounts/<slug:account_id>', AccountDetail.as_view(), name='account_detail'),

    #student list
    path('students',ListStudent.as_view(), name='list_student'),
    path('students/<slug:student_id>', StudentDetail.as_view(), name='student_detail'),
    #create studen
    # path('create_student',CreateStudent.as_view(), name='create_student'),
]