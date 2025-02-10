from __future__ import annotations

from rest_framework import generics

from ..models.projects import Project
from ..serializers.projects import ProjectSerializer


class ProjectCreateView(generics.CreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProjectListView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProjectDetailView(generics.RetrieveAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ProjectUpdateView(generics.UpdateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class ProjectDeleteView(generics.DestroyAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
