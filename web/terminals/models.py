from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from docker import errors


class RunningDockerTerminalsManager(models.Manager):
    def get_queryset(self):
        return super(
            RunningDockerTerminalsManager, self
        ).get_queryset().filter(started=True, exited=False)


class DockerTerminal(models.Model):
    """
    Represents a Terminal, using a Docker container.
    """
    owner = models.ForeignKey(User, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    container_id = models.CharField(max_length=64, blank=True)
    container_image = models.CharField(max_length=100)
    command = models.CharField(blank=True, max_length=255)
    started = models.BooleanField(default=False)
    exited = models.BooleanField(default=False)

    objects = models.Manager()
    running_objects = RunningDockerTerminalsManager()

    @property
    def container_meta_data(self):
        if self.exited or not self.started:
            return {}
        try:
            resp = settings.DOCKER_CLIENT.inspect_container(self.container_id)
            if not resp['State']['Running']:
                self.exited = True
                self.save()
            return resp
        except errors.NotFound as er:
            self.exited = True
            self.save()
        except APIError:
            return {}

    @property
    def running(self):
        return self.started and not self.exited

    @property
    def attach_url(self):
        return 'ws://{}/containers/{}/attach/ws'.format(
            settings.DOCKER_HOST, self.container_id
        )

    @property
    def attach_url_secure(self):
        return 'wss://{}/containers/{}/attach/ws'.format(
            settings.DOCKER_HOST, self.container_id
        )
