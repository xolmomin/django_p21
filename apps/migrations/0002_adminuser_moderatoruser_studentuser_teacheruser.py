# Generated by Django 5.0.6 on 2024-06-04 10:15

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("apps", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AdminUser",
            fields=[],
            options={
                "verbose_name": "Admin",
                "verbose_name_plural": "Admins",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("apps.user",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="ModeratorUser",
            fields=[],
            options={
                "verbose_name": "Moderator",
                "verbose_name_plural": "Moderators",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("apps.user",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="StudentUser",
            fields=[],
            options={
                "verbose_name": "Student",
                "verbose_name_plural": "Students",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("apps.user",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="TeacherUser",
            fields=[],
            options={
                "verbose_name": "Teacher",
                "verbose_name_plural": "Teachers",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("apps.user",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]