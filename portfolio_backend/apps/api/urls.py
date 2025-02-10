from __future__ import annotations

from django.urls import path

from .views.comments import CommentCreateView
from .views.comments import CommentDeleteView
from .views.comments import CommentDetailView
from .views.comments import CommentListView
from .views.comments import CommentUpdateView
from .views.posts import PostCreateView
from .views.posts import PostDeleteView
from .views.posts import PostDetailView
from .views.posts import PostListView
from .views.posts import PostUpdateView
from .views.projects import ProjectCreateView
from .views.projects import ProjectDeleteView
from .views.projects import ProjectDetailView
from .views.projects import ProjectListView
from .views.projects import ProjectUpdateView
from .views.services import ServiceCreateView
from .views.services import ServiceDeleteView
from .views.services import ServiceDetailView
from .views.services import ServiceListView
from .views.services import ServiceUpdateView

urlpatterns = [
    # Urls for Service model
    path('service/create', ServiceCreateView.as_view(), name='service'),
    path('service/', ServiceListView.as_view(), name='service-list'),
    path('service/<int:pk>/',
         ServiceDetailView.as_view(),
         name='service-detail'),
    path('service/<int:pk>/update',
         ServiceUpdateView.as_view(),
         name='service-update'),
    path('service/<int:pk>/delete',
         ServiceDeleteView.as_view(),
         name='service-delete'),

    # Urls for Project model
    path('project/create', ProjectCreateView.as_view(), name='project'),
    path('project/', ProjectListView.as_view(), name='project-list'),
    path('project/<int:pk>/',
         ProjectDetailView.as_view(),
         name='project-detail'),
    path('project/<int:pk>/update',
         ProjectUpdateView.as_view(),
         name='project-update'),
    path('project/<int:pk>/delete',
         ProjectDeleteView.as_view(),
         name='project-delete'),

    # Urls for Post model
    path('post/create', PostCreateView.as_view(), name='post'),
    path('post/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),

    # Urls for Comment model
    path('comment/create', CommentCreateView.as_view(), name='comment'),
    path('comment/', CommentListView.as_view(), name='comment-list'),
    path('comment/<int:pk>/',
         CommentDetailView.as_view(),
         name='comment-detail'),
    path('comment/<int:pk>/update',
         CommentUpdateView.as_view(),
         name='comment-update'),
    path('comment/<int:pk>/delete',
         CommentDeleteView.as_view(),
         name='comment-delete'),
]
