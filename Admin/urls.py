from django.urls import path
from .views import CreateStudent, Delete, ListAccount, ListStudent, Register

urlpatterns= [

    # account management
    path('register', Register.as_view(), name='register'),
    path('delete', Delete.as_view(), name='delete'),

    # account list
    path('list_account',ListAccount.as_view(), name='list_account'),

    #student list
    path('list_student',ListStudent.as_view(), name='list_student'),
    #create studen
    path('create_student',CreateStudent.as_view(), name='create_student'),
]