import json
from rest_framework import serializers
from reversion.models import Revision, Version

from .models import Choice, Poll


class VersionSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['versions'] = VersionSerializer(
            Version.objects.get_for_object(instance), many=True).data
        return data

class PollSerializer(VersionSerializer):
    class Meta:
        model = Poll
        fields = '__all__'


class ChoiceSerializer(VersionSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


class RevisionSerializer(serializers.ModelSerializer):
    """Holds metadata like user(creator), created_at and comment"""
    class Meta:
        model = Revision
        fields = '__all__'

class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = '__all__'

    def to_representation(self, instance):
        # data = super().to_representation(instance)
        # data['serialized_data'] = json.loads(data['serialized_data'])
        return {
            "data": instance.field_dict,
            "revision": RevisionSerializer(instance.revision).data,
        }
