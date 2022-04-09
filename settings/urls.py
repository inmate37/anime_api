from rest_framework.routers import DefaultRouter

from django.contrib import admin
from django.conf import settings
from django.urls import (
    path,
    include,
)
from django.conf.urls.static import static


urlpatterns = [
    path(settings.ADMIN_SITE_URL, admin.site.urls),
    path('', include('auths.urls')),
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
# router = DefaultRouter(
#     trailing_slash=False
# )
# app_name = 'router'


# urlpatterns += [
#     path(
#         'api/v1/',
#         include((router.urls, app_name), namespace='v1')
#     )
# ]
