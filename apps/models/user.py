from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, TextChoices, ImageField, DateField, Model, EmailField, BooleanField


class User(AbstractUser):
    class Type(TextChoices):
        ADMIN = 'admin', 'Admin'
        MODERATOR = 'moderator', 'Moderator'
        TEACHER = 'teacher', 'Teacher'
        STUDENT = 'student', 'Student'

    class Gender(TextChoices):
        MALE = 'male', 'Male'
        FEMALE = 'female', 'Female'

    phone = CharField(max_length=25, blank=True, null=True)
    type = CharField(max_length=15, choices=Type.choices, default=Type.STUDENT)
    image = ImageField(upload_to='users/%Y/%m/%d/', default='users/default.png')
    gender = CharField(max_length=15, default=Gender.MALE)
    birth_date = DateField(null=True, blank=True)
    email = EmailField(unique=True)
    is_active = BooleanField(default=False)

    class Meta:
        unique_together = [
            ('email', 'is_active')
        ]
