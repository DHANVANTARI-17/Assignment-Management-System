# Generated by Django 4.2.2 on 2024-04-11 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_remove_assignments_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='assignments',
            field=models.ManyToManyField(blank=True, to='users.assignments'),
        ),
    ]