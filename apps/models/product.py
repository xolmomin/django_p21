from django.db.models import ForeignKey, FloatField, CASCADE, DateTimeField, TextField, \
    PositiveSmallIntegerField
from django.db.models.functions import Now

from apps.models.base import SlugBaseModel


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
