from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views as core_views
from .views import (register_view,login_view, StudentListView, StudentDetailView, StudentCreateView,
                    AttendanceListView, AttendanceCreateView, GradeListView, GradeCreateView,SubjectListView,SubjectCreateView,SubjectDetailView
                    ,TeacherListView,TeacherDetailView,TeacherCreateView,ClassListview,ClassCreateView,ParentListView,ParentCreateView,StaffListView,StaffCreateView)
from accounts import views as accounts_views
urlpatterns = [
    path('', accounts_views.register_view, name="register"),
    path('dashbord/', accounts_views.admin_dashboard , name='dashboard'),
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
    path("teachers/create",TeacherCreateView.as_view(),name="teacher-create"),
    path('classes/',ClassListview.as_view(),name='class-list'),
    path('classes/create',ClassCreateView.as_view(),name='class-create'),
    path('parents/', ParentListView.as_view(),name='parent-list'),
    path('parents/create',ParentCreateView.as_view(),name='parent-create'),
    path('staffs/', StaffListView.as_view(),name='staff-list'),
    path('staffs/create',StaffCreateView.as_view(),name='staff-create')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
