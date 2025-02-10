from __future__ import annotations

from rest_framework import serializers

from ..models.services import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
