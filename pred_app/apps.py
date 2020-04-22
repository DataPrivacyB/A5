from django.apps import AppConfig


class PredAppConfig(AppConfig):
    name = 'pred_app'

    def ready(self):
        import userRegistration.signals