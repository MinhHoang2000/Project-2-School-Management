from django.urls import path
from rest_framework.renderers import TemplateHTMLRenderer
from .views import Login, Home, Logout

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', Login.as_view(), name='Login'),
    path('logout/', Logout.as_view(), name='logout'),
]