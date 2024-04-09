from django.urls import path

from courses.views import dashboard, create_or_update_test
from . import views

urlpatterns = [
    path('', views.course_list, name='courses'),
    path('dashboard/', dashboard, name='dashboard'),
    path('<slug:course_slug>/', views.course_detail, name='course_detail'),
    path('<slug:course_slug>/test/<slug:test_slug>', views.test_detail, name='test_detail'),
    path('<slug:course_slug>/lecture/<slug:lecture_slug>', views.lecture_detail, name='lecture_detail'),
    path('<slug:course_slug>/test/create/', create_or_update_test, name='create_test'),
]
