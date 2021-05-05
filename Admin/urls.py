from django.urls import path
from .views import AccountDetail, ListAccount, ListStudent, StudentDetail

urlpatterns= [

    # account management
    # path('register', Register.as_view(), name='register'),
    # path('delete', Delete.as_view(), name='delete'),

    # account list
    path('list_account',ListAccount.as_view(), name='list_account'),
    path('account_detail/<slug:account_id>', AccountDetail.as_view(), name='account_detail'),

    #student list
    path('list_student',ListStudent.as_view(), name='list_student'),
    path('student_detail/<slug:student_id>', StudentDetail.as_view(), name='student_detail'),
    #create studen
    # path('create_student',CreateStudent.as_view(), name='create_student'),
]