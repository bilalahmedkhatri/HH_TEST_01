from django.db import models
import random
import string

STATUS = ((0, 'CONVERTED'), (1, 'PENDING'), (2, 'FAILED'))

def generate_short_code(length=6):
    while True:
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        if not ShortenedURL.objects.filter(short_code=code).exists():
            return code

class ShortenedURL(models.Model):
    original_url = models.URLField()
    complate_link = models.URLField(max_length=100)
    status = models.PositiveIntegerField(choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    short_code = models.CharField(max_length=10, unique=True, default=generate_short_code)

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"


