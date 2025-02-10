from __future__ import annotations

from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path('api/', include('portfolio_backend.apps.api.urls')),
    path('admin/', admin.site.urls),
]
