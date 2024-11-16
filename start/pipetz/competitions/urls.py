from django.urls import path
from .views import competitions
from .views import get_active_competitions
from . import views 

urlpatterns = [
    path('', views.competitions, name='competitions'),
    path('competitions/<int:test_id>/take_test/', views.take_test, name='take_test'),
    path('competitions/test_success', views.test_success, name='test_success'),
    path('view_submissions/', views.view_submissions, name='view_submissions'),
    path('grade_submission/<int:submission_id>/', views.grade_submission, name='grade_submission'),
    path('get_active_competitions/', get_active_competitions, name='get_active_competitions'),
    path('create_test/', views.create_test, name='create_test'),
    path('test/<int:test_id>/', views.test_detail, name='test_detail'),
    path('admin/grade_submissions/<int:student_id>/', views.view_grade_submissions, name='view_grade_submissions'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),

]

# M7TAQNa7