# Generated by Django 5.0.6 on 2024-06-11 12:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apps", "0003_alter_user_options_alter_user_email_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomProduct",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="products/%Y/%m/%d/"
                    ),
                ),
                ("price", models.IntegerField(db_default=0, default=0)),
            ],
        ),
    ]