# Generated by Django 4.2.13 on 2024-05-13 22:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="gamingsession",
            name="grade",
            field=models.IntegerField(
                default=1,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(9),
                ],
            ),
            preserve_default=False,
        ),
    ]