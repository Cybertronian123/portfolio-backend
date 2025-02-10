from __future__ import annotations

from rest_framework import generics

from ..models.comments import Comments
from ..serializers.comments import CommentSerializer


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CommentDetailView(generics.RetrieveAPIView):
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class CommentUpdateView(generics.UpdateAPIView):
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class CommentDeleteView(generics.DestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
