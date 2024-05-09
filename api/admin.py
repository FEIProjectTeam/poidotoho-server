from django.contrib import admin

from api.models import GamingSession


@admin.register(GamingSession)
class GamingSessionAdmin(admin.ModelAdmin):
    list_display = ["nickname", "score", "time_left", "created_at", "updated_at"]
    fields = ["nickname", "score", "time_left", "created_at", "updated_at"]
    readonly_fields = ["created_at", "updated_at"]
