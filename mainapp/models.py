from django.db import models
from django.core.exceptions import ValidationError


class Badge(models.Model):
    badge_name = models.CharField(verbose_name="Badge name" ,max_length=30)
    badge_desc = models.TextField(verbose_name="Badge description")
    badge_photo = models.ImageField(verbose_name="Badge photo", upload_to='badgeimages')
    badge_url = models.URLField(verbose_name="Badge link",null=True)
    badge_upload_datetime = models.TimeField(auto_now_add=True)
