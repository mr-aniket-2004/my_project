# Generated by Django 5.1 on 2024-10-01 06:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='free_course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme1', models.ImageField(blank=True, null=True, upload_to='coursetheme')),
                ('youtube1', models.CharField(blank=True, max_length=500, null=True)),
                ('theme2', models.ImageField(blank=True, null=True, upload_to='coursetheme')),
                ('youtube2', models.CharField(blank=True, max_length=500, null=True)),
                ('theme3', models.ImageField(blank=True, null=True, upload_to='coursetheme')),
                ('youtube3', models.CharField(blank=True, max_length=500, null=True)),
                ('theme4', models.ImageField(blank=True, null=True, upload_to='coursetheme')),
                ('youtube4', models.CharField(blank=True, max_length=500, null=True)),
                ('theme5', models.ImageField(blank=True, null=True, upload_to='coursetheme')),
                ('youtube5', models.CharField(blank=True, max_length=500, null=True)),
                ('core', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.course')),
            ],
        ),
    ]
