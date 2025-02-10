from __future__ import annotations

from rest_framework import generics

from ..models.posts import Posts
from ..serializers.posts import PostSerializer


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PostDetailView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class PostUpdateView(generics.UpdateAPIView):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class PostDeleteView(generics.DestroyAPIView):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
