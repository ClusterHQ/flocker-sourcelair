from django.conf.urls import url, include
from rest_framework import generics, permissions, routers, viewsets

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


router = routers.DefaultRouter(trailing_slash=True)
router.register(r'terminals', DockerTerminalViewSet,
                base_name='dockerterminal')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]
