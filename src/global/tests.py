from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import SiteSettings


class SiteSettingsTestCase(TestCase):

    def test_save_single_record(self):
        site_settings = SiteSettings.objects.create(
            name="My Site",
            tagline="Welcome to My Site",
            description="This is a test site",
            logo="logo.png",
            logo_dark="logo_dark.png",
            logo_light="logo_light.png",
        )

        with self.assertRaises(ValidationError):
            SiteSettings.objects.create(
                name="Another Site",
                tagline="Welcome to Another Site",
                description="This is another test site",
                logo="another_logo.png",
                logo_dark="another_logo_dark.png",
                logo_light="another_logo_light.png",
            )

        self.assertEqual(SiteSettings.objects.count(), 1)
        self.assertEqual(SiteSettings.objects.first(), site_settings)
