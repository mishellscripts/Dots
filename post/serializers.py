from rest_framework import serializers

from . import models


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        extra_kwargs = {
            'status': {'write_only': True},
        }
        fields = (
            'text',
            'created_at',
            'user',
        )