from rest_framework import serializers

from terminals import models


class DockerTerminalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.DockerTerminal
        read_only_fields = ('id', 'created', 'last_updated', 'container_id',
                            'container_meta_data', 'started', 'exited', 'url',
                            'attach_url', 'attach_url_secure',)
        fields = read_only_fields + ('container_image', 'command',)

    def update(self, instance, validated_data):
        validated_data.pop('container_image')
        validated_data.pop('command')
        return super(DockerTerminalSerializer, self).update(
            instance, validated_data
        )
