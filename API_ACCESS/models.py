from django.db import models


STATUS = ((0, 'CONVERTED'), (1, 'PENDING'), (2, 'FAILED'))

class URL(models.Model):
    original_url = models.URLField()
    short_url = models.URLField(max_length=200, unique=True)
    status = models.PositiveIntegerField(choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'URL'
        verbose_name_plural = 'URLs'

    def get_absolute_url(self):
        return ('')


class Image(models.Model):
    image = models.ImageField(upload_to="images", height_field=None, width_field=None, max_length=None)
    created_at = models.DateTimeField(auto_now_add=True)  

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
