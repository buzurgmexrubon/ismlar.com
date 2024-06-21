# Generated by Django 4.2.13 on 2024-06-21 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("origins", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Name",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                ("meaning", models.TextField(max_length=10000, verbose_name="Meaning")),
                (
                    "origin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="names",
                        to="origins.origin",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]