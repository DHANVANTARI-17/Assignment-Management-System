from django.db import models
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import AbstractUser,PermissionsMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _ 
from django.conf import settings
import os
from datetime import datetime, date
from django.contrib.auth import get_user_model
# User = get_user_model()

#Create your models here.

class CustomUser(AbstractUser):
    is_student=models.BooleanField(default=True)
    is_teacher=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    # username=models.CharField(default='00000',max_length=5,unique=True)
    type =(
    ('Computer Engineering','Computer Engineering'),
    ('Information Technology','Information Technology'),
    ('Electronics and telecommunication','Electronics and telecommunication')
)
    FIRST_FIELD_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4)
    )
    
    # Define choices for the second field
    SECOND_FIELD_CHOICES = (
        ('FE', 'First Year'),
        ('SE', 'Second Year'),
        ('TE', 'Third Year'),
        ('BE', 'Final Year')
    )
    year=models.CharField(max_length=50,default='FE',choices=SECOND_FIELD_CHOICES)
    branch=models.CharField(default='Computer engineering',max_length=40,choices=type)
    Division=models.IntegerField(default =1,choices=FIRST_FIELD_CHOICES)
    first_name=models.CharField(default="NA",max_length=200)
    last_name=models.CharField(default="NA",max_length=200)
    roll_number=models.IntegerField(default='00000')
    username=models.CharField(default='00000',max_length=5,unique=True)
    email = models.EmailField(default='pict@gmail.com',unique=True)# Ensur)e email is unique
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    # is_active=models.BooleanField(default=True)
   
    def save(self, *args, **kwargs):
        is_new = not self.pk  # Check if the user is being created for the first time

        super().save(*args, **kwargs)  # Save the user first

        if self.is_student:
            student_instance, created = Student.objects.get_or_create(
                user=self)
            if created:
                student_instance.save()
            # Set any additional fields for the Student instance here, if needed
        elif self.is_teacher:
            teacher_instance, created = Teacher.objects.get_or_create(
                user=self)
            if created:
                teacher_instance.save()
        
class Subjects(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Batch(models.Model):
    name=models.CharField(default='A1',max_length=2)
    # teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE) 
    subjects=models.ManyToManyField(Subjects,related_name='teachers')
    batch = models.ManyToManyField(Batch, related_name='teachers_batch')
    def allocate_subject(self, subject):
        self.subjects.add(subject)

    def allocate_batch(self, batch):
        self.batch.add(batch)
        
class Assignments(models.Model):
    batch=models.ForeignKey(Batch,default=1,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subjects,on_delete=models.CASCADE)
    # location = models.FilePathField(blank=True,default=settings.MEDIA_ROOT)
    # teacher=models.OneToOneField(to=Teacher,blank=True,default=1,on_delete=models.CASCADE)
    title = models.CharField(max_length=200,default='Title')
    description = models.TextField(default='Not available')
    deadline = models.DateField(blank=True, null=True)
    # batch=models.ManyToManyField(Batch)
    status_choices = (
        ('UPLOADED', 'Uploaded'),
        ('NOT_UPLOADED', 'Not Uploaded')
    )
    status = models.CharField(max_length=20, choices=status_choices, default='NOT_UPLOADED')
    def __str__(self):
        return f"Assignment for {self.subject.name}"  


class Student(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    batch=models.ForeignKey(Batch, on_delete=models.CASCADE, blank=True, null=True) 
    subjects = models.ManyToManyField(Subjects, related_name='students')
    # assignments=models.ManyToManyField(Assignments, blank=True)
    
    def __str__(self):
        return str(self.id) + ' - ' + self.user.first_name + ' ' + self.user.last_name
    
    def allocate_subjects(self):
        if self.user.branch == 'Computer engineering' and self.user.year == 'FE':
            subjects = Subjects.objects.filter(name__in=['Introduction to Programming', 'Data Structures', 'Discrete Mathematics'])
        elif self.user.branch == 'Computer Engineering' and self.user.year == 'SE':
            subjects = Subjects.objects.filter(name__in=['Database Systems', 'Operating Systems', 'Computer Networks'])
    # add mor e conditions for other branches and years
        else:
            subjects = []

    # Add the subjects to the student's subjects field
        for subject in subjects:
            self.subjects.add(subject)
            
    def allocate_batch(self):
        user=self.user
        # Extract the third last digit from the roll number as division
        roll_number_str = str(user.roll_number)

    # Extract the third last digit from the roll number as division
        division = user.Division

        # Extract the last two digits from the roll number
        last_two_digits = int(str(user.roll_number)[-2:])

        # Determine the batch based on the last two digits
        if 0 <= last_two_digits <= 21:
            batch = 'E'
        elif 22 <= last_two_digits <= 43:
            batch = 'F'
        elif 44 <= last_two_digits <= 61:
            batch = 'G'
        else:
            batch = 'H'

        # Concatenate the batch and division to form the final batch
        final_batch_name = batch + str(division)

        
        batch = Batch.objects.get(name=final_batch_name)
        
    # Add the batch to the student's batches field
        self.batch=batch
        self.save()
        return batch


class TeacherAllocation(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('subject', 'batch')
         
    def __str__(self):
        return str("{self.teacher.name} is allocated to {self.subject.name} for batch {self.batch.name}")
    
class AssignmentSubmission(models.Model):
    assignment = models.ForeignKey(Assignments, on_delete=models.CASCADE)
    teacher=models.ForeignKey(Teacher,blank=True, null=True,on_delete=models.CASCADE)
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # subject=models.OneToOneField(Subjects,blank=True, null=True,on_delete=models.CASCADE)
    submission_deadline = models.DateField(blank=True, null=True)
    # location=models.CharField(null=True,blank=True,max_length=500)
    submitted_on=models.CharField(blank=True,null=True,max_length=20)
    filename = models.CharField(blank=True,null=True,max_length=70)
    submitted=models.BooleanField(default=False)
    evaluation=models.BooleanField(default=False)
    feedback = models.TextField(blank=True)
    marks=models.IntegerField(blank=True,null=True)
    # def save(self, *args, **kwargs):
    #     if self.location:
    #         self.location = f"{self.student.branch}_{self.student.year}_{self.assignment.subject}_{self.assignment.batch}_{self.student.roll_number}"

    #     # Check if the provided address is valid
    #         if not os.path.isdir(os.path.join(settings.MEDIA_ROOT, self.location)):
    #             # If not valid, create the required folders
    #             os.makedirs(os.path.join(settings.MEDIA_ROOT, self.location))

    #         super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.student.username} - {self.assignment.title}"

    class Meta:
        unique_together = ('assignment', 'student')