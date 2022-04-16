from typing import Any

from rest_framework.routers import DefaultRouter

from django.contrib import admin
from django.conf import settings
from django.urls import (
    path,
    include,
)
from django.conf.urls.static import static

from auths.views import CustomUserViewSet


urlpatterns = [
    path(settings.ADMIN_SITE_URL, admin.site.urls),
] + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
) + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]


# ------------------------------------------------
# API-Endpoints
#
app_name = 'router'

router: DefaultRouter = DefaultRouter(
    trailing_slash=False
)
router.register('auths', CustomUserViewSet)

urlpatterns += [
    path(
        'api/v1/',
        include((router.urls, app_name), namespace='v1')
    )
]
