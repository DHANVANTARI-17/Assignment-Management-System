# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.utils import timezone
from .models import CustomUser,Student,Teacher,TeacherAllocation,Subjects,Batch,Assignments,AssignmentSubmission
from django.core.files.storage import FileSystemStorage

class StudentRegistrationForm(UserCreationForm):
    # Choices for the 'year' field
    YEAR_CHOICES = (
        ('FE', 'First Year'),
        ('SE', 'Second Year'),
        ('TE', 'Third Year'),
        ('BE', 'Final Year')
    )
    
    # Choices for the 'branch' field
    BRANCH_CHOICES = (
        ('Computer Engineering', 'Computer Engineering'),
        ('Information Technology', 'Information Technology'),
        ('Electronics and Telecommunication', 'Electronics and Telecommunication')
    )

    # Choices for the 'division' field
    DIVISION_CHOICES = (
        (1, 'Division 1'),
        (2, 'Division 2'),
        (3, 'Division 3'),
        (4, 'Division 4')
    )

    # Additional fields for user registration
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}))
    roll_number=forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # Additional fields for student details
    year = forms.ChoiceField(choices=YEAR_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    branch = forms.ChoiceField(choices=BRANCH_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    Division = forms.ChoiceField(choices=DIVISION_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=(('Male', 'Male'), ('Female', 'Female')), widget=forms.Select(attrs={'class': 'form-control'}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    address = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'gender', 'date_of_birth', 'address', 'phone_number','is_student','is_teacher','is_admin']

class Login(forms.Form):
    username = forms.IntegerField(
    widget=forms.TextInput(
        attrs={
            "class": "form-control"
        }
    )
)

    password = forms.CharField(
    widget=forms.PasswordInput(
        attrs={
            "class": "form-control"
        }
    )
)

class TeacherAllocationForm(forms.ModelForm):
    subject = forms.ModelChoiceField(queryset=Subjects.objects.all())
    batch = forms.ModelChoiceField(queryset=Batch.objects.all())
    class Meta:
        model = TeacherAllocation
        fields = ['subject', 'batch']
        
class AssignmentsForm(forms.ModelForm):
    title = forms.CharField(max_length=50, required=True)
    description = forms.CharField(max_length=500, required=True)
    deadline = forms.DateTimeField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),required=True)
    # location = forms.FilePathField(path=settings.MEDIA_ROOT)
    # subject=forms.HiddenInput()
    # batch=forms.HiddenInput()

    class Meta:
        model = Assignments
        fields = ['title', 'description', 'deadline']

    def __init__(self, *args, **kwargs):
        # Set default values for other fields
        super().__init__(*args, **kwargs)
        self.fields['status'] = forms.CharField(initial='NOT_UPLOADED', widget=forms.HiddenInput())

    def clean(self):
        cleaned_data = super().clean()
        deadline = cleaned_data.get('deadline')

        if deadline is not None:
            if deadline <= timezone.now():
                self.add_error('deadline', 'The deadline must be in the future.')

        return cleaned_data
    
# def dynamic_upload_to(instance, filename):
#     # Generate the dynamic address based on the instance (student) attributes
#     user = instance.user
#     address = f"{user.branch}_{user.year}_{instance.assignmentsubmission.subject}_{user.roll_number}"
#     return f"{address}/{filename}"

class CustomForm(forms.Form):
    assignment_file = forms.FileField(label='Upload Assignment', widget=forms.FileInput(attrs={'accept': '.pdf,.doc,.docx,.cpp'}))

#     def save(self, commit=True, upload_to=None):
#         # instance = super().save(commit=False)
#         # if upload_to:
#             # file_field = self.cleaned_data.get('assignment_field')
#             if file_field:
#                 fs = FileSystemStorage(location=upload_to)
#                 filename = fs.save(file_field.name, file_field)
#                 # instance.file_field = filename
#                 print("upload_to valid", file_field.name, filename.path) 
#             else:
#                 print("file_field not found")
#         # else:
#             # print("no upload_to found")
#         #if commit:
#             # instance.save()
#         #return instance
    
class StudentEvaluationform(forms.ModelForm):
    marks=forms.IntegerField()
    feedback=forms.CharField(max_length=200)
    class Meta:
        model=AssignmentSubmission
        fields=['marks','feedback']