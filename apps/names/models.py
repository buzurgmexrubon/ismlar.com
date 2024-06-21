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

    def __str__(self):
        return self.name
