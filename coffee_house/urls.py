from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.generic import RedirectView

from . import views
from .views import register, login_view, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('employees/', include('employees.urls')),
    path('courses/', include('courses.urls')),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('upgrade_role/<str:username>/', views.upgrade_role, name='upgrade_role'),
    path('', RedirectView.as_view(pattern_name='home'), name='redirect_home'),
]
