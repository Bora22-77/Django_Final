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
    path('teacher/fill_info', views.TeacherFillInforView.as_view(), name="fill_info"),
    path('student/fill_info_student', views.StudentFillInforView.as_view(), name="fill_info_student"),
    path('staff/fill_info_staff', views.StaffFillInforView.as_view(), name="fill_info_staff"),
    path('parent/fill_info_parent', views.ParentFillInforView.as_view(), name="fill_info_parent")
]

