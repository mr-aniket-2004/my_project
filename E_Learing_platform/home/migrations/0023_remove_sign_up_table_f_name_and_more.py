# Generated by Django 5.0.6 on 2024-08-15 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_remove_sign_up_table_p_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sign_up_table',
            name='f_name',
        ),
        migrations.RemoveField(
            model_name='sign_up_table',
            name='s_name',
        ),
    ]
