from __future__ import annotations

from django.urls import include
from django.urls import path

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
]
