# Generated by Django 5.0.6 on 2024-05-25 12:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("apps", "0002_product_is_premium"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProxyProduct",
            fields=[],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Premium Products",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("apps.product",),
        ),
    ]
