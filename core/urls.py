from django.urls import path
from . import views
from .views import (register_view,login_view, StudentListView, StudentDetailView, StudentCreateView,
                    AttendanceListView, AttendanceCreateView, GradeListView, GradeCreateView,SubjectListView,SubjectCreateView,SubjectDetailView
                    ,TeacherListView,TeacherDetailView,ClassListview,ClassCreateView,ParentListView,StaffListView)
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
    path("subjects/<int:pk>/",SubjectDetailView.as_view(),name='subject-detail'),
    path("teachers/",TeacherListView.as_view(),name='teacher_list'),
    path("teachers/<int:pk>", TeacherDetailView.as_view(),name='teacher-detail'),
    path('classes/',ClassListview.as_view(),name='class-list'),
    path('classes/create',ClassCreateView.as_view(),name='class-create'),
    path('parents/', ParentListView.as_view(),name='parent-list'),
    path('staffs/', StaffListView.as_view(),name='staff-list')
]
