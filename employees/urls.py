from django.urls import path

from . import views
from .views import intern_dashboard

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('intern_dashboard', intern_dashboard, name='intern_dashboard'),
]
