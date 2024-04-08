from django.contrib import admin
from django.urls import path, include

from . import views
from .views import register, login_view, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('employees/', include('employees.urls')),
    path('courses/', include('courses.urls')),
    path('register/', register, name='register'),
    path('profile', profile, name='profile'),
    path('login/', login_view, name='login'),
]
