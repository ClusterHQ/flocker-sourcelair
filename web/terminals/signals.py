import docker

from django.conf import settings


def terminal_pre_save(sender, instance, *args, **kwargs):
    """
    Creates the process, right before it being saved to the database and adds
    the created container id.
    """
    if instance.pk:
        return
    command = '/bin/bash -l {}'.format(instance.command)
    container = settings.DOCKER_CLIENT.create_container(
        instance.container_image, command=command, tty=True, stdin_open=True,
        volumes=['/data'],
        host_config=docker.utils.create_host_config(binds={
                'user_data_{}'.format(instance.owner.pk): {
                    'bind': '/data',
                    'mode': 'rw',
                },
            }),
        volume_driver='flocker',
        working_dir='/data',
    )
    settings.DOCKER_CLIENT.start(container=container.get('Id'))
    instance.started = True
    instance.container_id = container.get('Id')
