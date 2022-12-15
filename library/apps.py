from django.apps import AppConfig


class LibraryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'library'

class UserConfig(AppConfig):
    name = 'user'

    def ready(self):
        import user.signals



