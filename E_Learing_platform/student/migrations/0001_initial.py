# Generated by Django 5.0.6 on 2024-08-23 15:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0023_remove_sign_up_table_f_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_couser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('core_subject', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.course')),
            ],
        ),
    ]
