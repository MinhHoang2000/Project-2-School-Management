import django
from django.urls.conf import include
from rest_framework.authtoken import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('Account.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('', include('django.contrib.auth.urls')),
]
