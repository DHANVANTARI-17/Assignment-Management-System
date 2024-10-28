
from datetime import datetime  
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm, Login,TeacherAllocationForm,AssignmentsForm, CustomForm,StudentEvaluationform
from django.contrib.auth import authenticate,get_user_model
from django.contrib.auth import login as auth_login
from django.views.decorators.csrf import csrf_protect
from .models import Student,Teacher,TeacherAllocation,Batch,Subjects,Assignments,AssignmentSubmission
from django.contrib.auth.decorators import login_required
import os
from django.contrib.auth import settings
from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotFound


User = get_user_model()

def register_student(request):
    msg=None
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            msg="successfully registered."
            form.save()
            user = User.objects.get(username=form.cleaned_data['username'])  # Assuming username is unique
            if user.is_student:
                # Retrieve the corresponding Student object
                student = Student.objects.get(user=user)
                # Call the allocate_subjects method for the student
                student.allocate_subjects()
                student.allocate_batch()
            return redirect('login') 
        else:
            msg="Form entries not valid"# Redirect to student dashboard
    else:
        msg="get request"
        form = StudentRegistrationForm()
    return render(request, 'Register.html', {'form': form,'msg':msg})

def Studentlogin(request):
    form = Login(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.filter(username=username).first()
            if user is not None:
                if check_password(password,user.password) and user.is_student:
                    student = Student.objects.get(user=user)
                    auth_login(request, user)
                    return redirect('dashboard')
                elif check_password(password,user.password) and user.is_teacher:
                    auth_login(request,user)
                    return redirect('teacher_dashboard')
                else:
                    msg="Invalid Credentials."
            else:
                msg = "Invalid credentials2"
        else:
            msg="Invalid credentials3"
    return render(request, 'login.html', {'form': form, 'msg': msg})
            
# def register_teacher(request):
#     if request.method == 'POST':
#         form = TeacherRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('teacher_dashboard')  # Redirect to teacher dashboard
#     else:
#         form = TeacherRegistrationForm()
#     return render(request, 'registration/register_teacher.html', {'form': form})

@login_required
def dashboard(request):
    User = get_user_model()
    user = request.user
    student = Student.objects.get(user=user)
    batch=student.batch
    subjects = student.subjects.all()
    # subjectwise_submissions = {}
    # subjectwise_assignments = {}
    # teachers={}
    # for subject in subjects:
    #     # Fetch submissions for the current subject
    #     subject_assignments= Assignments.objects.filter(batch=batch,subject=subject)
    #     subjectwise_assignments[subject] = subject_assignments
    #     subject_submissions = AssignmentSubmission.objects.filter(student=user, assignment__in=subject_assignments)
    #     subjectwise_submissions[subject] = subject_submissions
    # teachers = {}
    # for subject in subjects:
    #     assignments = subject.assignments_set.filter(batch=student.batch)
    #     subject_teachers = set()
    #     for assignment in assignments:
    #         subject_teachers.add(assignment.teacher)
    #     teachers[subject] = subject_teachers
    context = {
        'student': student,
        'subjects': subjects,
        'user':user,
        'batch':batch,
        # 'subjectwise_submissions':subjectwise_submissions,
        # 'subjectwise_assignments':subjectwise_assignments,
        # 'teachers':teachers
        }
    return render(request, 'Dashboard.html', context)

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def about(request):
    return render(request,'about.html')

def course(request):
    return render(request,'courses.html')

def calendar(request):
    return render(request,'Calender.html')

def contact(request):
    return render(request,'contact.html')

def assignment(request,subject_id, batch_id):
    user=request.user
    student = Student.objects.get(user=user)
    batch=student.batch
    subject=Subjects.objects.get(id=subject_id)
    assignments=Assignments.objects.filter(batch=batch,subject=subject)
    assignment_submissions={}
    print(assignments)
    for assignment_item in assignments:
        submissionassignments = AssignmentSubmission.objects.filter(assignment=assignment_item)
        if submissionassignments.exists():
            for submissionassignment in submissionassignments:
                assignment_submissions[assignment_item.id]=submissionassignment

    context = {'user': user, 'assignments': assignments,'batch':batch,'subject':subject,'assignment_submissions':assignment_submissions}
    return render(request, 'assignment.html', context)
# def profile(request):
#     return render(request,'profile.html')


def view(request,subject_id,batch_id,assignment_id):
    user=request.user
    assignment=Assignments.objects.get(id=assignment_id)
    assignment_submission=AssignmentSubmission.objects.get(assignment=assignment,student=user,submitted=True)
    return render(request,'view.html',{'assignment':assignment,'assignment_submission':assignment_submission})

def upload(request,subject_id,batch_id,assignment_id):
    user=request.user
    subject=Subjects.objects.get(id=subject_id)
    batch=Batch.objects.get(id=batch_id)
    assignments=Assignments.objects.filter(subject=subject,batch=batch)
    assignmentsubmission={}
    assignment_1=Assignments.objects.get(id=assignment_id)
    if assignment_1 is None:
        return HttpResponseNotFound("Assignment not found.")
    for assignment in assignments:
        submissionassignments_queryset = AssignmentSubmission.objects.filter(assignment=assignment, student=user)
        if submissionassignments_queryset.exists():
            assignmentsubmission[assignment.id] = submissionassignments_queryset.first()
        else:
            assignmentsubmission[assignment.id] = None
    if request.method=="POST":
        form = CustomForm(request.POST, request.FILES)
        if form.is_valid():
            # Dynamically allocate address based on user, subject, and roll number
            # assignmentsubmission=AssignmentSubmission.objects.get(student='user')
            user = request.user
            assignment_submission=AssignmentSubmission.objects.get(assignment=assignment_1,student=user)
            address = f"{user.branch}_{user.year}_{assignment_1.subject}_{user.roll_number}"
            print(assignment_submission)
            # address = f"media/"
            # assignment.address = address
            # assignmentfile = form.save(address)
            assignment_submission.submitted=True
            current_date = datetime.date
            assignment_submission.submitted_on=str(current_date)
            # form.save()
            # user=teacher.user
            f = request.FILES["assignment_file"]
            assignment_submission.save()
            assignment_submission.filename=f.name
            print("file name is", f.name, " address is ", address)
            with open(address+f.name, 'wb+') as destination:   
                for chunk in f.chunks(): 
                    destination.write(chunk)   
            print("Redirecting to dashboard.")
            return redirect('dashboard')
    else:
        form = CustomForm()
            
    context={'subject':subject,'batch':batch,'assignment':assignment,'user':user,'form':form}
    return render(request,'upload.html',context)

def list(request):
    return render(request,'list.html')

def teacher_dashboard(request):
    User = get_user_model()
    user = request.user
    teacher = Teacher.objects.get(user=user)
    subjects = teacher.subjects.all()  # Corrected line
    allocations = TeacherAllocation.objects.filter(teacher=teacher)
    if request.method == 'POST':
        form = TeacherAllocationForm(request.POST)
        if form.is_valid():
            allocation=form.save(commit=False)
            allocation.teacher=teacher
            allocation.save()
            teacher.subjects.add(allocation.subject)
            teacher.batch.add(allocation.batch)
            return redirect('teacher_dashboard')  # Redirect to a success page
    else:
        form = TeacherAllocationForm()
    context = {'teacher': teacher, 'subjects': subjects,'allocations':allocations,'user':user,'form':form}
    return render(request, 'Teacher_dashboard.html', context)

def class_page(request, subject_id, batch_id):
    user=request.user
    # subject=user.teacher.subject
    subject = Subjects.objects.get(id=subject_id)
    batch = Batch.objects.get(id=batch_id)
    assignments = Assignments.objects.filter(subject=subject, batch=batch)
    if request.method=="POST":
        form=AssignmentsForm(request.POST)
        if form.is_valid():
            assignment=form.save(commit=False)
            # assignment.location=f"{settings.MEDIA_ROOT}/{user.year}/{batch}/{subject}"
            # assignment.teacher=Teacher.objects.get(user=user)
            # assignment.subject=subject
            assignment.subject=subject
            assignment.status="NOT_UPLOADED"
            assignment.batch=batch
            assignment.save()
            print(batch)
            students_in_batch=Student.objects.filter(batch=batch)
            print(students_in_batch)
            teacher=Teacher.objects.get(user=user)
            for student in students_in_batch:
                AssignmentSubmission.objects.create(
                    # subject=subject,
                    teacher=teacher,
                    # location=None,
                    assignment=assignment,
                    student=student.user,
                    submission_deadline=assignment.deadline,
                    evaluation=False,
                    file='',  # Set the default value for the file field
                    submitted=False,  # Set the default value for the submitted field  # Set the default value for the evaluation field
                    feedback='',  # Set the default value for the feedback field
                    marks=0,
                )
                print(f"Created submission for", {student})
            redirect('class_page', subject_id=subject_id, batch_id=batch_id)
    else:
        form = AssignmentsForm()
    return render(request, 'class.html', {'form':form ,'subject': subject, 'batch': batch,'assignments':assignments})

def teacher_view(request):
    return render(request,'teacher_view.html')

def teacher_view1(request,subject_id,batch_id,assignment_id):
    subject=Subjects.objects.get(id=subject_id)
    batch=Batch.objects.get(id=batch_id)
    assignment=Assignments.objects.get(id=assignment_id)
    assignment_submissions=AssignmentSubmission.objects.filter(assignment=assignment)
    user_listfname={}
    user_listlname={}
    for assignment_submission in assignment_submissions:
        student=assignment_submission.student
        user_listfname[assignment_submission]=student.first_name
        user_listlname[assignment_submission]=student.last_name
    if request.method=="POST":
        form=StudentEvaluationform(request.POST or None)
        assignment_submission_id_1=request.POST.get('assignment_submission_id')
        assignment_submission=AssignmentSubmission.objects.get(id=assignment_submission_id_1)
        print(assignment_submission)
        if form.is_valid():
            assignment_submission_form=form.save(commit=False)
            print(assignment_submission_form.marks)
            assignment_submission.marks=assignment_submission_form.marks
            assignment_submission.feedback=assignment_submission_form.feedback
            assignment_submission.evaluation=True
            assignment_submission.save()
            return redirect('teacher-view',subject_id=subject_id, batch_id=batch_id,assignment_id=assignment_id)
    else:
        form=StudentEvaluationform()
    return render(request,'Teacher-view.html',{'assignment_submissions':assignment_submissions,'assignment':assignment,'user_listfname':user_listfname,'user_listlname':user_listlname,'form':form})

