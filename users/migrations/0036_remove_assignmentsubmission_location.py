# Generated by Django 4.2.2 on 2024-04-12 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0035_assignmentsubmission_location_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignmentsubmission',
            name='location',
        ),
    ]