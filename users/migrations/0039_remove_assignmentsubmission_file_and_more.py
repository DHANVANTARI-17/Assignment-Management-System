# Generated by Django 4.2.2 on 2024-04-12 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0038_assignmentsubmission_teacher_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignmentsubmission',
            name='file',
        ),
        migrations.AddField(
            model_name='assignmentsubmission',
            name='filename',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
