# Run this after migrations to create demo users and data:
# python manage.py shell < init_data.py
from core.models import User, SchoolClass, ParentProfile, StudentProfile, TeacherProfile, Subject
if not User.objects.filter(username='admin').exists():
    admin = User.objects.create_superuser('admin','admin@example.com','adminpass', role='admin', first_name='Admin')
if not User.objects.filter(username='teacher1').exists():
    u = User.objects.create_user('teacher1','t1@example.com','pass1234', role='teacher', first_name='Teacher')
    TeacherProfile.objects.create(user=u)
if not User.objects.filter(username='parent1').exists():
    pu = User.objects.create_user('parent1','p1@example.com','pass1234', role='parent', first_name='Parent')
    parent = ParentProfile.objects.create(user=pu)
if not SchoolClass.objects.exists():
    c = SchoolClass.objects.create(name='Grade 10', section='A')
if not User.objects.filter(username='student1').exists():
    su = User.objects.create_user('student1','s1@example.com','pass1234', role='student', first_name='Sok', last_name='Rith')
    StudentProfile.objects.create(user=su, school_class=SchoolClass.objects.first(), roll_number='10', parent=ParentProfile.objects.first())
print('Demo data created (if missing).')
