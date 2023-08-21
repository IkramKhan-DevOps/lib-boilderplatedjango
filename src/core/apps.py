from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'src.core'
    verbose_name = 'Core'
    verbose_plural = 'Core'
    default_auto_config = 'django.db.models.BigAutoField'

    def ready(self):
        import src.core.signals
