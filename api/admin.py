from django.contrib import admin

from api.models import GamingSession, School


@admin.register(GamingSession)
class GamingSessionAdmin(admin.ModelAdmin):
    list_display = [
        "nickname",
        "grade",
        "school",
        "score",
        "time_left",
    ]
    fields = [
        "nickname",
        "grade",
        "school",
        "score",
        "time_left",
        "created_at",
        "updated_at",
    ]
    readonly_fields = ["created_at", "updated_at"]


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ["name"]
    fields = ["name"]
    search_fields = ["name"]
