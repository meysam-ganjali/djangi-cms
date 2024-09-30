from django.apps import AppConfig


class SliderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.slider'
    verbose_name = 'مدیریت اسلایدرها'

    def ready(self):
        import apps.slider.signals
