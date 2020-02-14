from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = '{{ project_name }}.users'

    def ready(self):
        try:
            import authentication.signals  # noqa F401
        except ImportError:
            pass
