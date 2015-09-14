from django.conf.urls import url, include
from rest_framework import generics, permissions, routers, viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from terminals import models
from terminals import serializers


class DockerTerminalViewSet(viewsets.ModelViewSet):
    model = models.DockerTerminal
    serializer_class = serializers.DockerTerminalSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_queryset(self):
        return models.DockerTerminal.objects.filter(
            owner=self.request.user
        ).order_by('-created')

    def perform_create(self, serializer):
        """
        Override to set the user.
        """
        serializer.save(owner=self.request.user)

    @list_route(methods=['post'])
    def get_or_create(self, request):
        serializer = self.serializer_class(data=self.request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        queryset = self.get_queryset().filter(started=True, exited=False)
        terminal = None
        try:
            terminal = queryset.get()
        except self.model.DoesNotExist:
            pass
        except self.model.MultipleObjectsReturned:
            for terminal in queryset.all()[1:]:
                terminal.kill(raise_exception=False)
            terminal = queryset.first()
        if terminal and terminal.container_meta_data and terminal.running:
            serializer = self.serializer_class(
                terminal, context={'request': request}
            )
            return Response(serializer.data)
        self.perform_create(serializer=serializer)
        return Response(serializer.data)


router = routers.DefaultRouter(trailing_slash=True)
router.register(r'terminals', DockerTerminalViewSet,
                base_name='dockerterminal')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]
