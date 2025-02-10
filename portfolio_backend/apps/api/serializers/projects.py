from __future__ import annotations

from rest_framework import serializers

from ..models.projects import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
