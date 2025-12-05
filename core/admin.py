from django.contrib import admin
from .models import User, SchoolClass, TeacherProfile, StudentProfile, ParentProfile, Subject, Attendance, Grade,StaffProfile

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','role','is_staff','is_active')
    list_filter = ('role','is_staff','is_active')

admin.site.register(SchoolClass)
admin.site.register(TeacherProfile)
admin.site.register(StudentProfile)
admin.site.register(ParentProfile)
admin.site.register(Subject)
admin.site.register(Attendance)
admin.site.register(Grade)
admin.site.register(StaffProfile)
