# Generated by Django 4.2.2 on 2024-04-12 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0031_alter_customuser_division'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='Division',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=1),
        ),
    ]
