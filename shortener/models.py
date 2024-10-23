from django.db import models
import random
import string

def generate_short_code(length=6):
    while True:
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        if not ShortenedURL.objects.filter(short_code=code).exists():
            return code

class ShortenedURL(models.Model):
    original_url = models.URLField(max_length=2048)
    
    # def get_name(self, ):
    
    short_code = models.CharField(max_length=10, unique=True, default=generate_short_code)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"
