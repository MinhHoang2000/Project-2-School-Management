from django.urls import path
from .views import Delete, Register

urlpatterns= [
    path('register', Register.as_view(), name='register'),
    path('delete', Delete.as_view(), name='delete'),
]