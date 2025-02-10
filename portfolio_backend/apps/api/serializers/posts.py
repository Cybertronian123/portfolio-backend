from __future__ import annotations

from rest_framework import serializers

from ..models.posts import Posts


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'
