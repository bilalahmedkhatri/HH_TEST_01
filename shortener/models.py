from django.db import models
from django.utils import timezone
import random
import string

STATUS = ((0, 'CONVERTED'), (1, 'PENDING'), (2, 'FAILED'))

def generate_short_code(length=6):
    while True:
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        if not ShortenedURL.objects.filter(short_code=code).exists():
            return code

class ShortenedURL(models.Model):
    name = models.CharField(max_length=100)
    original_url = models.URLField(max_length=1000)
    status = models.PositiveIntegerField(choices=STATUS, default=0)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    short_code = models.CharField(max_length=10, unique=True, default=generate_short_code)

    def __str__(self):
        return self.short_code


