from django.db import models

from apps.common.models import BaseModel
from django.utils.translation import gettext_lazy as _

from apps.origins.models import Origin


class Name(BaseModel):
    name = models.CharField(
        _("Name"),
        max_length=100,
    )
    meaning = models.TextField(
        _("Meaning"),
        max_length=10_000,
    )
    origin = models.ForeignKey(
        Origin,
        on_delete=models.CASCADE,
        related_name="names",
    )
    is_active = models.BooleanField(_("Is Active"), default=True)
    likes_count = models.IntegerField(_("Likes Count"), default=0)
    views_count = models.IntegerField(_("Views Count"), default=0)
    forms_of_the_name = models.ForeignKey(
        "NameForm",
        on_delete=models.CASCADE,
        related_name="forms",
        null=True,
        blank=True,
    )
    famous_persons = models.ForeignKey(
        "FamousPeople",
        on_delete=models.CASCADE,
        related_name="people",
        null=True,
        blank=True,
    )
    # slug = models.SlugField(_("Slug"),)
    GENDERS = (
        ("M", "Male"),
        ("F", "Female"),
    )
    gender = models.CharField(_("Gender"), choices=GENDERS, max_length=1)

    def __str__(self):
        return self.name


class Like(BaseModel):
    user = models.ForeignKey(
        "CustomUser", on_delete=models.CASCADE
    )  # Link to the user who liked
    name = models.ForeignKey("Name", on_delete=models.CASCADE)  # Link to the liked name


class CustomUser(models.Model):
    pass


class FamousPeople(models.Model):
    name = models.CharField(
        _("Name"),
        max_length=100,
        unique=True,
    )
    occupation = models.CharField(_("Occupation"), max_length=100)

    def __str__(self):
        return self.name


# class Occupation(models.Model):
#     name = models.CharField(
#         _("Name"),
#         max_length=100,
#         unique=True,
#     )
#     description = models.TextField(max_length=3000)
#     image_url = models.URLField(
#         _("Image URL"),
#     )
#     date_of_birth = models.DateField(_("Date of birth"))
#     date_of_death = models.DateField(_("Date of death"), blank=True)
#
#     def __str__(self):
#         return self.occupation


class NameForm(BaseModel):
    name_form = models.CharField(
        _("Name form"),
        max_length=100,
    )

    def __str__(self):
        return self.name_form
