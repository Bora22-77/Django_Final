from django.urls import path
from . import views
from .views import (register_view,login_view, StudentListView, StudentDetailView, StudentCreateView,
                    AttendanceListView, AttendanceCreateView, GradeListView, GradeCreateView,SubjectListView,SubjectCreateView,SubjectDetailView
                    ,TeacherListView)
from accounts import views
urlpatterns = [
    path('', views.register_view, name="register"),
    path('dashbord/',views.admin_dashboard , name='dashboard'),
    path('students/', StudentListView.as_view(), name='students'),
    path('students/add/', StudentCreateView.as_view(), name='student-add'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('attendance/', AttendanceListView.as_view(), name='attendance-list'),
    path('attendance/add/', AttendanceCreateView.as_view(), name='attendance-add'),
    path('grades/', GradeListView.as_view(), name='grades'),
    path('grades/add/', GradeCreateView.as_view(), name='grade-add'),
    path("subjects/", SubjectListView.as_view(), name="subject_list"),
    path("subjects/create/", SubjectCreateView.as_view(), name="subject_create"),
    path("subjects/<int:pk>/",SubjectDetailView.as_view,name='subject-detail'),
    path("teachers/",TeacherListView.as_view(),name='teacher_list')
]
