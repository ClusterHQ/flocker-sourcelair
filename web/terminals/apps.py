from django.apps import AppConfig
from django.db.models.signals import pre_save


class TerminalsAppConfig(AppConfig):
    name = 'terminals'
    verbose_name = 'Terminals'

    def ready(self):
        from terminals import signals
        DockerTerminal = self.get_model('DockerTerminal')
        pre_save.connect(signals.terminal_pre_save, sender=DockerTerminal)
