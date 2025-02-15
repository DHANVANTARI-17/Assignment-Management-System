# Generated by Django 4.2.2 on 2024-04-11 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_assignments_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignments',
            name='location',
        ),
        migrations.AddField(
            model_name='assignmentsubmission',
            name='evaluation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='assignmentsubmission',
            name='submitted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='assignmentsubmission',
            name='file',
            field=models.FileField(blank=True, upload_to='media/'),
        ),
    ]
