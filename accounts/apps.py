from django.apps import AppConfig

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    # Agrega la importación de signals.py para que las señales sean registradas
    def ready(self):
        import accounts.signals
