# Generated by Django 4.2.2 on 2024-04-11 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_teacherallocation_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='batch',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.batch'),
        ),
    ]
