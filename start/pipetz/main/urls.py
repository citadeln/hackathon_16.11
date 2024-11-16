from django.urls import include, path
from . import views
from .views import profile_view
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls,),
    path('about', views.about, name='about'),
    path('competitions/', include('competitions.urls')),
    path('create_test/', include('competitions.urls'), name='create_test'),
    path('register_participant/', views.register_participant, name='register_participant'),
    path('teacher_students/', views.teacher_students, name='teacher_students'),
    path('accounts/profile/', profile_view, name="profile"),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/registration/', views.signup, name='registration'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
]
