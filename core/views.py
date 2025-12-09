from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import StudentProfile, TeacherProfile, SchoolClass, Attendance, Grade
from .forms import StudentProfileForm, AttendanceForm, GradeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from .models import User, TeacherProfile, StudentProfile, ParentProfile, SchoolClass,Attendance, Grade,StaffProfile
from .models import Subject
from .forms import SubjectForm ,ClassForm,TeacherForm,ParentForm,StaffForm
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Redirect based on role
            if user.role == "admin":
                return redirect("admin/dashboard")
            elif user.role == "teacher":
                return redirect("teacher_dashboard")
            elif user.role == "student":
                return redirect("student_dashboard")
            elif user.role == "parent":
                return redirect("parent_dashboard")
            elif user.role == "staff":
                return redirect("staff_dashboard")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "accounts/login.html")

def register_view(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        # Check if username exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        # Create User
        user = User.objects.create(
            username=username,
            password=make_password(password),
            role=role,
            first_name=full_name,
        )

        #Create Profile depending on role
        if role == "teacher":
            TeacherProfile.objects.create(user=user)

        elif role == "student":
            StudentProfile.objects.create(user=user)

        elif role == "parent":
            ParentProfile.objects.create(user=user)

        messages.success(request, "Registration successful! Please login.")
        return redirect("login")

    return render(request, "accounts/register.html")

def logout_view(request):
    logout(request)
    return redirect("login")

class StudentListView(LoginRequiredMixin, ListView):
    model = StudentProfile
    template_name = 'core/student_list.html'
    context_object_name = 'students'

class StudentDetailView(LoginRequiredMixin, DetailView):
    model = StudentProfile
    template_name = 'core/student_detail.html'
    context_object_name = 'student'

class StudentCreateView(LoginRequiredMixin, CreateView):
    model = StudentProfile
    form_class = StudentProfileForm
    template_name = 'core/student_form.html'
    success_url = reverse_lazy('students')

class AttendanceListView(LoginRequiredMixin, ListView):
    model = Attendance
    template_name = 'core/attendance_list.html'
    context_object_name = 'attendances'

class AttendanceCreateView(LoginRequiredMixin, CreateView):
    model = Attendance
    form_class = AttendanceForm
    template_name = 'core/attendance_form.html'
    success_url = reverse_lazy('attendance-list')

class GradeListView(LoginRequiredMixin, ListView):
    model = Grade
    template_name = 'core/grade_list.html'
    context_object_name = 'grades'

class GradeCreateView(LoginRequiredMixin, CreateView):
    model = Grade
    form_class = GradeForm
    template_name = 'core/grade_form.html'
    success_url = reverse_lazy('grades')

# ---------- LIST ----------
class SubjectListView(LoginRequiredMixin, ListView):
    model = Subject
    template_name = "core/subject_list.html"
    context_object_name = "subjects"

# ---------- CREATE ----------
class SubjectCreateView(LoginRequiredMixin, CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = "core/subject_form.html"
    success_url = reverse_lazy("subject_list")
class SubjectDetailView(LoginRequiredMixin, DetailView):
    model = Subject
    form_class = SubjectForm
    template_name = "core/subject_form.html"
    success_url = reverse_lazy("subject_list")

class TeacherListView(LoginRequiredMixin,ListView):
    model=TeacherProfile
    template_name="core/teacher_list.html"
    context_object_name="teachers"
class TeacherDetailView(LoginRequiredMixin,DetailView):
    model= TeacherProfile
    template_name ="core/teacher_detail.html"
    context_object_name ="teacher"
class TeacherCreateView(LoginRequiredMixin,CreateView):
    model = TeacherProfile
    form_class = TeacherForm
    template_name ="core/teacher_form.html"
    success_url = reverse_lazy("teachers")
class ClassListview(LoginRequiredMixin,ListView):
    model = SchoolClass
    template_name ="core/class_list.html"
    context_object_name ="classes"
class ClassCreateView(LoginRequiredMixin, CreateView):
    model = SchoolClass
    form_class = ClassForm
    template_name = "core/class_form.html"
    success_url = reverse_lazy("class_list")
class ParentListView(LoginRequiredMixin, ListView):
    model = ParentProfile
    template_name = "core/parent_list.html"
    context_object_name = "parents"
class ParentCreateView(LoginRequiredMixin,CreateView):
    model = ParentProfile
    form_class = ParentForm
    template_name ="core/parent_form.html"
    success_url = reverse_lazy("parents")
class StaffListView(LoginRequiredMixin, ListView):
    model = StaffProfile
    template_name = "core/staff_list.html"
    context_object_name = "staffs"
class StaffCreateView(LoginRequiredMixin,CreateView):
    model = StaffProfile
    form_class = StaffForm
    template_name ="core/staff_form.html"
    success_url = reverse_lazy("staffs")

