from django.contrib import admin

from api.models import GamingSession


@admin.register(GamingSession)
class GamingSessionAdmin(admin.ModelAdmin):
    pass
