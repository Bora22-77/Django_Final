from django.urls import path
from . import views
from .views import HomeView

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('admin/dashboard/',HomeView.as_view(),name='dashboard'),
    path('register/', views.register_view, name="register"),
    path('teacher/dashboard/', views.teacher_dashboard, name="teacher_dashboard"),
    path('student/dashboard/', views.student_dashboard, name="student_dashboard"),
    path('parent/dashboard/', views.parent_dashboard, name="parent_dashboard"),
    path('admin/dashboard/', views.admin_dashboard, name="admin_dashboard"),
    path('staff/dashboard/', views.staff_dashboard, name="staff_dashboard"),
]
