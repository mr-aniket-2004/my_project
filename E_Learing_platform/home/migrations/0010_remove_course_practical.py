# Generated by Django 5.0.6 on 2024-07-25 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_rename_practicalcategroy_course_practical'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='practical',
        ),
    ]
