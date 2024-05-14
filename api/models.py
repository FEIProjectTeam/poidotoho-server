from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class School(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class GamingSession(models.Model):
    nickname = models.CharField(max_length=32)
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(9)])
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    score = models.IntegerField()
    time_left = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nickname

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
