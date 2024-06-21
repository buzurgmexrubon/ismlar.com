from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.continents.models import Continent


class Origin(models.Model):
    name = models.CharField(
        _("Origin Name"),
        max_length=100,
        unique=True,
    )
    continent = models.ForeignKey(
        Continent,
        on_delete=models.CASCADE,
        related_name="origins",
    )

    def __str__(self):
        return self.name
