from django.contrib import admin
from django.urls import path, include

from employees.views import intern_dashboard
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('employees/', include('employees.urls')),
    path('courses/intern_dashboard/', intern_dashboard, name='intern_dashboard'),
    path('courses/', include('courses.urls')),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
]
