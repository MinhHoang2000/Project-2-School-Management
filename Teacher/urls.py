from django.urls import path, re_path
from .views import ListTeachingInfo

urlpatterns = [
    path('teaching-info', ListTeachingInfo.as_view(), name='teaching_information'),
    # re_path(r'filter(?P<classroom>)', ListTeachingInfoFilter.as_view()),
]