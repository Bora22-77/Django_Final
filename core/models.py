from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin','Admin'),
        ('teacher','Teacher'),
        ('student','Student'),
        ('parent','Parent'),
        ('staff','Staff'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    phone = models.CharField(max_length=20, blank=True)

    def is_teacher(self):
        return self.role == 'teacher'
    def is_student(self):
        return self.role == 'student'

class SchoolClass(models.Model):
    name = models.CharField(max_length=50)
    section = models.CharField(max_length=10, blank=True)
    def __str__(self):
        return f"{self.name}{(' - ' + self.section) if self.section else ''}"

class Subject(models.Model):
    name = models.CharField(max_length=120)
    code = models.CharField(max_length=50, blank=True)
    def __str__(self): return self.name

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject, blank=True)
    bio = models.TextField(blank=True)
    def __str__(self): return self.user.get_full_name() or self.user.username

class ParentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    def __str__(self): return self.user.get_full_name() or self.user.username

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.SET_NULL, null=True, blank=True)
    roll_number = models.CharField(max_length=20, blank=True)
    parent = models.ForeignKey(ParentProfile, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self): return self.user.get_full_name() or self.user.username

class StaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    bio = models.TextField(blank=True)
    def __str__(self): return self.user.get_full_name() or self.user.username
    
class Attendance(models.Model):
    STATUS = (('present','Present'),('absent','Absent'),('late','Late'))
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS, default='present')
    remark = models.TextField(blank=True)
    class Meta:
        unique_together = ('student','date')
    def __str__(self): return f"{self.student} - {self.date} - {self.status}"

class Grade(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    term = models.CharField(max_length=50, default='Term 1')
    marks_obtained = models.FloatField()
    max_marks = models.FloatField(default=100)
    def __str__(self): return f"{self.student} - {self.subject} - {self.marks_obtained}/{self.max_marks}"
