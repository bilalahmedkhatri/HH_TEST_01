from django.db import models
from django.utils import timezone


class ShortenedURLModel(models.Model):
    name = models.CharField(max_length=100)
    original_url = models.URLField(max_length=1000)
    url_bytes = models.BinaryField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    short_code = models.CharField(max_length=6, unique=True)
