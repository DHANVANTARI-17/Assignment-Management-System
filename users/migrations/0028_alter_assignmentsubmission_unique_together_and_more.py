# Generated by Django 4.2.2 on 2024-04-11 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_alter_assignmentsubmission_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='assignmentsubmission',
            unique_together={('assignment', 'student')},
        ),
        migrations.RemoveField(
            model_name='assignmentsubmission',
            name='subject',
        ),
    ]