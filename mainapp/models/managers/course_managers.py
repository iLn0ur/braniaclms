__all__ = ['CoursesManager']

from django.db import models


class CoursesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)
