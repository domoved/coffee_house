from django.urls import path

from . import views

urlpatterns = [
    path('', views.role_list, name='role_list'),
    path('<int:role_id>/', views.role_detail, name='role_detail'),
]
