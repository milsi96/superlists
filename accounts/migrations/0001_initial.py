# Generated by Django 4.2.5 on 2023-10-20 14:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "email",
                    models.EmailField(
                        max_length=254, primary_key=True, serialize=False
                    ),
                ),
            ],
        ),
    ]
