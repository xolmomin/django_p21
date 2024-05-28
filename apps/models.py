from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, ForeignKey, FloatField, SlugField, CASCADE, DateTimeField, TextField, \
    PositiveSmallIntegerField, \
    TextChoices
from django.db.models.functions import Now
from django.utils.text import slugify


class User(AbstractUser):
    class Type(TextChoices):
        ADMIN = 'admin', 'Admin'
        MODERATOR = 'moderator', 'Moderator'
        TEACHER = 'teacher', 'Teacher'
        STUDENT = 'student', 'Student'

    phone = CharField(max_length=25, blank=True, null=True)
    type = CharField(max_length=15, choices=Type.choices, default=Type.STUDENT)


class SlugBaseModel(Model):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True, editable=False)

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        while self.__class__.objects.filter(slug=self.slug).exists():
            self.slug += '-1'
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name


class Category(SlugBaseModel):
    parent = ForeignKey('self', CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'


class Product(SlugBaseModel):
    price = FloatField()
    category = ForeignKey('apps.Category', CASCADE)
    description = TextField(blank=True, null=True)
    discount = PositiveSmallIntegerField(default=0, help_text='Chegirma foizi')
    updated_at = DateTimeField(auto_now_add=True, db_default=Now())
    created_at = DateTimeField(auto_now=True, db_default=Now())

    @property
    def current_price(self):
        return self.price - (self.price * self.discount) // 100
