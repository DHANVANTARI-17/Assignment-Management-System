# Generated by Django 4.2.2 on 2024-04-12 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_alter_customuser_division'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='Division',
            field=models.IntegerField(choices=[(1, 'Division 1'), (2, 'Division 2'), (3, 'Division 3'), (4, 'Division 4')], default=1),
        ),
    ]