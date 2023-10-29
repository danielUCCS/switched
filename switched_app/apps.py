from django.apps import AppConfig


class SwitchedAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'switched_app'
