from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.blog'
    verbose_name = 'مدیریت مقاله ها'

    def ready(self):
        import apps.blog.signals