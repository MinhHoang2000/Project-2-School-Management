import django
from django.urls.conf import include
from rest_framework.authtoken import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', include('Admin.urls')),
    path('account/', include('Account.urls')),
]
