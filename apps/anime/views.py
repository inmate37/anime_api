from typing import Optional
from datetime import datetime

from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response as DRF_Response
from rest_framework.request import Request as DRF_Request

from django.db.models import QuerySet

from anime.models import Anime
from anime.serializers import (
    AnimeSerializer,
)
from anime.permissions import (
    AnimePermission,
)
from abstracts.paginators import (
    AbstractPageNumberPaginator,
    AbstractLimitOffsetPaginator,
)


class AnimeViewSet(ViewSet):
    """ViewSet for Anime."""

    permission_classes: tuple = (
        AnimePermission,
    )
    queryset: QuerySet[Anime] = \
        Anime.objects.get_not_deleted()

    serializer_class: AnimeSerializer = \
        AnimeSerializer

    pagination_class: AbstractPageNumberPaginator = \
        AbstractPageNumberPaginator

    def get_queryset(self) -> QuerySet[Anime]:
        return self.queryset

    @action(
        methods=['get'],
        detail=False,
        url_path='list-2',
        permission_classes=(
            permissions.AllowAny,
        )
    )
    def list_2(self, request: DRF_Request) -> DRF_Response:
        """Handles GET-request to list Anime."""

        paginator: AbstractLimitOffsetPaginator = \
            AbstractLimitOffsetPaginator()

        objects: list = paginator.paginate_queryset(
            self.get_queryset(),
            request
        )
        serializer: AnimeSerializer = \
            self.serializer_class(
                objects,
                many=True
            )
        response: DRF_Response = \
            paginator.get_paginated_response(
                serializer.data
            )
        return response

    def list(self, request: DRF_Request) -> DRF_Response:
        """Handles GET-request to list Anime."""

        paginator: AbstractPageNumberPaginator = \
            self.pagination_class()

        objects: list = paginator.paginate_queryset(
            self.get_queryset(),
            request
        )
        serializer: AnimeSerializer = \
            self.serializer_class(
                objects,
                many=True
            )
        response: DRF_Response = \
            paginator.get_paginated_response(
                serializer.data
            )
        return response
