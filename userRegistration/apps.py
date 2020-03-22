from django.apps import AppConfig


class UserregistrationConfig(AppConfig):
    name = 'userRegistration'

    def ready(self):
        import userRegistration.signals