from django.contrib import admin
from .models import ShortenedURLModel
# Register your models here.


@admin.register(ShortenedURLModel)
class ShortenedURLModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_code', 'url_bytes',
                    'original_url', 'created_at')
