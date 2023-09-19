import reversion
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from reversion.models import Version

from . import models, serializers


class RevisionViewSet(ModelViewSet):
    def perform_create(self, serializer):
        with reversion.create_revision():
            if self.request.user.is_authenticated:
                reversion.set_user(self.request.user)
            return super().perform_create(serializer)

    def perform_update(self, serializer):
        with reversion.create_revision():
            if self.request.user.is_authenticated:
                reversion.set_user(self.request.user)
            return super().perform_update(serializer)

    def perform_destroy(self, instance):
        with reversion.create_revision():
            if self.request.user.is_authenticated:
                reversion.set_user(self.request.user)
            return super().perform_destroy(instance)



class PollViewSet(RevisionViewSet):
    model = models.Poll
    queryset = models.Poll.objects.filter(is_active=True)
    serializer_class = serializers.PollSerializer


class ChoiceViewSet(RevisionViewSet):
    model = models.Choice
    queryset = models.Choice.objects.filter(is_active=True)
    serializer_class = serializers.ChoiceSerializer


class VersionViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    model = Version
    queryset = Version.objects.all()
    serializer_class = serializers.VersionSerializer
