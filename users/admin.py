from django.contrib import admin
from .models import CustomUser,Student,Teacher,Subjects,Assignments,Batch,AssignmentSubmission
# Register your models here.
from django.contrib import admin
from .models import Assignments
from .forms import AssignmentsForm

admin.site.register(AssignmentSubmission)
admin.site.register(Assignments)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(CustomUser)
admin.site.register(Subjects)
admin.site.register(Batch)


