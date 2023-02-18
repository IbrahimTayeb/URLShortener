# models.py
from django.db import models
import shortuuid

class ShortenedURL(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=22, unique=True)

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = shortuuid.uuid()[:7]
        super(ShortenedURL, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.short_url