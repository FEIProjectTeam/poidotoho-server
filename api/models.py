from django.db import models


class GamingSession(models.Model):
    nickname = models.CharField(max_length=32)
    score = models.IntegerField()
    time_left = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
