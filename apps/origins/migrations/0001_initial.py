# Generated by Django 4.2.13 on 2024-06-21 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("continents", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Origin",
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
                (
                    "name",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="Origin Name"
                    ),
                ),
                (
                    "continent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="origins",
                        to="continents.continent",
                    ),
                ),
            ],
        ),
    ]
