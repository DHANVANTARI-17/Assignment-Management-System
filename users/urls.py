from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('class/<int:subject_id>/<int:batch_id>/<int:assignment_id>/teacher-view/',views.teacher_view1,name='teacher-view'),
    path('assignment/<int:subject_id>/<int:batch_id>/<int:assignment_id>/upload/',views.upload,name='upload'),
    path('register/', views.register_student, name='register_student'),
    # path('register/', views.register_teacher, name='register_teacher'),
    path('login/',views.Studentlogin,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('about/',views.about,name='about'),
    path('calendar/',views.calendar,name='calendar'),
    path('contact/',views.contact,name='contact'),
    path('course/',views.course,name='course'),
    path('assignment/<int:subject_id>/<int:batch_id>/',views.assignment,name='assignment'),
    path('assignment/<int:subject_id>/<int:batch_id>/<int:assignment_id>/view/',views.view,name='view'),
    path('list/',views.list,name='list'),
    path('class/<int:subject_id>/<int:batch_id>/',views.class_page,name='class_page'),
    path('teacher_dashboard/',views.teacher_dashboard,name='teacher_dashboard'),
    path('teacher_view/',views.teacher_view,name='teacher_view')
    
    # path('Teacherlogin/',views.Teacher,name='Teacher')
]
