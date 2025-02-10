from __future__ import annotations

from rest_framework import generics

from ..models.services import Service
from ..serializers.services import ServiceSerializer


class ServiceCreateView(generics.CreateAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ServiceListView(generics.ListAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ServiceDetailView(generics.RetrieveAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ServiceUpdateView(generics.UpdateAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class ServiceDeleteView(generics.DestroyAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
