# Generated by Django 4.2.2 on 2024-04-12 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0033_assignmentsubmission_submitted_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignmentsubmission',
            name='teacher',
        ),
    ]