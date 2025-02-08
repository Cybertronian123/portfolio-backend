from __future__ import annotations

if IN_DOCKER:  # type: ignore
    assert MIDDLEWARE[:1] == [  # type: ignore
        'django.middleware.security.SecurityMiddleware'
    ]
