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
        if hasattr(self, '_container_meta_data'):
            return getattr(self, '_contianer_meta_data')
        if self.exited or not self.started:
            return {}
        try:
            resp = settings.DOCKER_CLIENT.inspect_container(self.container_id)
            if not resp['State']['Running']:
                self.exited = True
                self.save()
            setattr(self, '_contianer_meta_data', resp)
            return resp
        except errors.NotFound:
            self.exited = True
            self.save()
        except errors.APIError:
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

    def kill(self, raise_exception=True):
        try:
            settings.DOCKER_CLIENT.kill(container=self.container_id)
        except errors.NotFound:
            self.exited = True
            self.save()
            if raise_exception:
                raise
        except errors.APIError:
            if raise_exception:
                raise
            return {}
