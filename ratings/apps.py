from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class RatingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ratings'
    verbose_name = _('profiles')

    def ready(self):
        import ratings.signals

