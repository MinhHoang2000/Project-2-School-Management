from django.urls import path
# from .views import AccountDetail, AchievementDetail, ListAccount, ListAchievement, ListStudent, ListStudentAchievement, StudentDetail
from Account.views import ListAccount, AccountDetail
from Student.views import ListStudent, StudentDetail, ListStudentAchievement
from Person.views import ListAchievement, AchievementDetail

urlpatterns= [

    # account list
    path('account',ListAccount.as_view(), name='list_account'),
    path('account/<slug:account_id>', AccountDetail.as_view(), name='account_detail'),

    #student list
    path(r'student',ListStudent.as_view(), name='list_student'),
    path(r'student/<slug:student_id>', StudentDetail.as_view(), name='student_detail'),
    path(r'student/<slug:student_pk>/achievement', ListStudentAchievement.as_view(), name='student_achievement__list'),
    
    # achievement list
     path('achievement',ListAchievement.as_view(), name='list_achievement'),
     path('achievement/<int:achievement_id>', AchievementDetail.as_view(), name='achievement_detail'),
    
]