from django.core.exceptions import ValidationError
from django.db import models


class SiteSettings(models.Model):
    name = models.CharField(max_length=255, default="Exarth")
    tagline = models.CharField(max_length=255, default="Your technology partner")
    description = models.TextField(default="No description added")

    logo = models.ImageField(upload_to='global/images/logos', null=True, blank=True)
    logo_dark = models.ImageField(upload_to='global/images/logos', null=True, blank=True)
    logo_light = models.ImageField(upload_to='global/images/logos', null=True, blank=True)
    favicon = models.ImageField(upload_to='global/images/favicons', null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Site Settings'

    def save(self, *args, **kwargs):
        if SiteSettings.objects.exists() and not self.pk:
            raise ValidationError("Only one record of SiteSettings can be saved.")
        super().save(*args, **kwargs)


