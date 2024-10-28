# Generated by Django 4.2.2 on 2024-03-29 09:27

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_student', models.BooleanField(default=True)),
                ('is_teacher', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='custom_user_groups', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='custom_user_permissions', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(choices=[('FE', 'First Year'), ('SE', 'Second Year'), ('TE', 'Third Year'), ('BE', 'Final Year')])),
                ('branch', models.CharField(choices=[(1, 'Computer Engineering'), (2, 'Information Technology'), (3, 'Electronics and telecommunication')], max_length=2)),
                ('Division', models.IntegerField(choices=[(1, 'Division 1'), (2, 'Division 2'), (3, 'Division 3'), (4, 'Division 4')])),
                ('name', models.CharField(max_length=200)),
                ('student', models.ManyToManyField(to='users.student')),
                ('teacher', models.ManyToManyField(to='users.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Assignments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('UPLOADED', 'Uploaded'), ('NOT_UPLOADED', 'Not Uploaded')], default='NOT_UPLOADED', max_length=20)),
                ('subject', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.subjects')),
                ('location', models.FilePathField(default='')),
                ('title', models.CharField(max_length=200, default='Title')),
                ('description', models.TextField(default='Not available')),
                ('deadline', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
