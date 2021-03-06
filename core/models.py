from django.db import models


class TimeStampedModel(models.Model):

    """ Time Stamped Model : used for common models in apps except for users"""

    created = models.DateTimeField(
        auto_now_add=True
    )  # when model is created, record now date, time
    updated = models.DateTimeField(
        auto_now=True
    )  # when model is updated, record now date, time

    class Meta:
        abstract = True
