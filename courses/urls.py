from django.urls import path

from courses.views import intern_dashboard, hr_manager_dashboard, create_or_update_test
from . import views

urlpatterns = [
    path('', views.course_list, name='courses'),
    path('<slug:course_slug>/', views.course_detail, name='course_detail'),
    path('courses/intern_dashboard/', intern_dashboard, name='intern_dashboard'),
    path('courses/hr_manager_dashboard/', hr_manager_dashboard, name='hr_manager_dashboard'),
    path('<slug:course_slug>/test/create/', create_or_update_test, name='create_test'),
]
