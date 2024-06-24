from django.contrib import admin

from apps.names.admin_mixins import ExportAsCSVMixin
from apps.names.models import Name


@admin.action(description="Active names")
def activate(model_admin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description="Inactive names")
def inactivate(model_admin, request, queryset):
    queryset.update(is_active=False)


@admin.register(Name)
class NameAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    actions = [
        activate,
        inactivate,
        "export_as_csv",
    ]
    list_display = (
        "pk",
        "name",
        "meaning",
        "origin",
        "get_continent",
        "is_active",
    )
    list_display_links = ("pk", "name")
    list_filter = (
        "origin",
        "is_active",
    )
    search_fields = (
        "name",
        "meaning",
        "origin",
        "get_continent",
    )
    ordering = ("pk",)
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "name",
                    "meaning",
                    "origin",
                ],
            },
        ),
        (
            "Extra options",
            {
                "fields": [
                    "is_active",
                ],
                "classes": ["collapse"],
                "description": "Extra options. Field 'is_active' is for soft delete",
            },
        ),
    ]

    def get_continent(self, obj):
        return obj.origin.continent.name

    def get_queryset(self, request):
        return Name.objects.select_related("origin").select_related("origin__continent")
