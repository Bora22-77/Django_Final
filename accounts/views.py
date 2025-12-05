from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import TeacherProfile, StudentProfile, ParentProfile,StaffProfile, SchoolClass,Attendance, Grade,User
from django.core.exceptions import ObjectDoesNotExist
# from .models import User

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Redirect based on role
            if user.role == "admin":
                return redirect("admin_dashboard")
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

def logout_view(request):
    logout(request)
    return redirect("login")

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/dashboard.html'
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['students_count'] = StudentProfile.objects.count()
        ctx['teachers_count'] = TeacherProfile.objects.count()
        ctx['classes_count'] = SchoolClass.objects.count()
        ctx['recent_attendance'] = Attendance.objects.order_by('-date')[:5]
        return ctx

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
        elif role == "staff":
            StaffProfile.objects.create(user=user)

        messages.success(request, "Registration successful! Please login.")
        return redirect("login")

    return render(request, "accounts/register.html")


# ------------------ DASHBOARDS ------------------

@login_required
def admin_dashboard(request):
    return render(request, "accounts/dashboard.html")

@login_required
def teacher_dashboard(request):
    teacher = TeacherProfile.objects.get(user=request.user)
    return render(request, "accounts/teacher_dashboard.html", {"teacher": teacher})

@login_required
def student_dashboard(request):
    student = StudentProfile.objects.get(user=request.user)
    grades = Grade.objects.filter(student=student)
    attendance = Attendance.objects.filter(student=student)
    return render(request, "accounts/student_dashboard.html", {
        "student": student,
        "grades": grades,
        "attendance": attendance,
    })

@login_required
def parent_dashboard(request):
    parent = ParentProfile.objects.get(user=request.user)
    children = StudentProfile.objects.filter(parent=parent)
    return render(request, "accounts/parent_dashboard.html", {"parent": parent, "children": children})

@login_required
def staff_dashboard(request):
    try:
        staff=request.user.staffprofile
    except ObjectDoesNotExist:
        staff=None
    return render(request, "accounts/staff_dashboard.html",{"staff" : staff})