from django.db import models
from django.core.exceptions import ValidationError


class Badge(models.Model):

    BADGE_CHOICES = (("markscard", "markscard"),("certificate","certificate"),("other","other"))

    badge_type = models.CharField(max_length = 20, choices = BADGE_CHOICES, default=2)

    badge_name = models.CharField(verbose_name="Badge name" ,max_length=30)
    badge_desc = models.TextField(verbose_name="Badge description")
    badge_photo = models.ImageField(verbose_name="Badge photo", upload_to='badgeimages', null=True)
    badge_url = models.URLField(verbose_name="Badge link",null=True, blank=True)
    badge_upload_datetime = models.TimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.badge_name
