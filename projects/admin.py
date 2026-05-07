from django.contrib import admin
from .models import Project, ContactMessage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_featured", "order", "updated_at")
    list_filter = ("category", "is_featured")
    list_editable = ("is_featured", "order")
    search_fields = ("title", "summary", "tools_used")
    prepopulated_fields = {"slug": ("title",)}

    fieldsets = (
        ("Overview", {
            "fields": ("title", "slug", "summary", "category", "image", "link")
        }),
        ("Interview Write-up", {
            "fields": (
                "business_problem",
                "tools_used",
                "key_features",
                "role_contribution",
                "biggest_challenge",
                "lessons_learned",
            )
        }),
        ("Display Settings", {
            "fields": ("is_featured", "order")
        }),
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "submitted_at", "is_read")
    list_filter = ("is_read", "submitted_at")
    search_fields = ("name", "email", "subject", "message")
    readonly_fields = ("name", "email", "subject", "message", "submitted_at")
