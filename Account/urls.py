from django.urls import path
from .views import ChangePassword, Login, Logout

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('change_password', ChangePassword.as_view(), name='change_password')
]