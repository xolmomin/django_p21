import uuid

from django.contrib.postgres.functions import RandomUUID
from django.core.validators import FileExtensionValidator
from django.db.models import Model, CharField, ForeignKey, UUIDField, FloatField, SlugField, CASCADE, ImageField, \
    DateTimeField, BooleanField
from django.db.models.functions import Now
from django.utils.text import slugify


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
    pass

    class Meta:
        ordering = '-id', 'name'
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'


class Product(SlugBaseModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4, db_default=RandomUUID(), editable=False)
    price = FloatField(help_text="Product narxi uzb so'mida")
    category = ForeignKey('apps.Category', CASCADE)
    is_premium = BooleanField(default=False, help_text="Premium userlar uchun")
    updated_at = DateTimeField(auto_now_add=True, db_default=Now())
    created_at = DateTimeField(auto_now=True, db_default=Now())

    @property
    def show_price(self):
        return int(self.price + 5)


class ProxyProduct(Product):
    class Meta:
        proxy = True
        verbose_name = 'Product'
        verbose_name_plural = 'Premium Products'


class ProductImage(Model):
    id = UUIDField(primary_key=True, db_default=RandomUUID(), editable=False)
    image = ImageField(upload_to='products/%Y/%m/%d/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    product = ForeignKey('apps.Product', CASCADE)
    updated_at = DateTimeField(auto_now_add=True, db_default=Now())
    created_at = DateTimeField(auto_now=True, db_default=Now())

    # def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    #     if self.id:
    #         product_image = ProductImage.objects.filter(id=self.id).first()
    #         if product_image.image.name != self.image.name:
    #             product_image.image.delete(False)
    #     super().save(force_insert, force_update, using, update_fields)

    def delete(self, using=None, keep_parents=False):
        self.image.delete(False)
        return super().delete(using, keep_parents)
