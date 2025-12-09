from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, StudentProfile, Attendance, Grade
from .models import Subject,SchoolClass,TeacherProfile,ParentProfile,StaffProfile

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','role','phone']

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['user','school_class','roll_number','parent']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student','date','status','remark']

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student','subject','term','marks_obtained','max_marks']


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ["name", "code"]
class ClassForm(forms.ModelForm):
    class Meta:
        model = SchoolClass
        fields = ["name","section"]
class TeacherForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = ["user","subjects","bio"]
class ParentForm(forms.ModelForm):
    class Meta:
        model = ParentProfile
        fields = ["user","phone"]
class StaffForm(forms.ModelForm):
    class Meta:
        model = StaffProfile
        fields = ["user","position","phone","bio"]

