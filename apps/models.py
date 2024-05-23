from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    price = models.FloatField(default=0)
    category = models.ForeignKey(Category, models.CASCADE)

    def __str__(self):
        return self.name


class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='members/')
    username = models.CharField(max_length=255)
    website = models.URLField(max_length=255)
    wallet_balance = models.FloatField()
    income_amount = models.FloatField()
    total_transaction = models.IntegerField()
