from django.contrib import admin
from .models import SiteSettings


class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'tagline', 'created_on')


admin.site.register(SiteSettings, SiteSettingsAdmin)
