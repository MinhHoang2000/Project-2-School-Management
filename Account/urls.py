from django.urls import path
from rest_framework.renderers import TemplateHTMLRenderer
from .views import ChangePassword, Login, Home, Logout

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('change_password/', ChangePassword.as_view(), name='change_password')
]