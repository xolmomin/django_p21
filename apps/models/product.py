from django.db.models import CharField, ImageField, Model, IntegerField, DateTimeField, JSONField, CASCADE
from django.db.models.functions import Now
from mptt.models import MPTTModel, TreeForeignKey

from django_ckeditor_5.fields import CKEditor5Field


class CustomProduct(Model):
    name = CharField(max_length=255)
    image = ImageField(upload_to='products/%Y/%m/%d/', null=True, blank=True)
    price = IntegerField(default=0, db_default=0)
    properties = JSONField(default=dict, null=True, blank=True)
    description = CKEditor5Field(null=True, blank=True)
    created_at = DateTimeField(auto_now=True, db_default=Now())


class CustomCategory(MPTTModel):
    name = CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
