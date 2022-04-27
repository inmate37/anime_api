from typing import Optional
from datetime import datetime

from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response as DRF_Response
from rest_framework.request import Request as DRF_Request

from django.db.models import QuerySet

from abstracts.validators import APIValidator
from abstracts.paginators import (
    AbstractPageNumberPaginator,
    AbstractLimitOffsetPaginator,
)
from anime.models import Anime
from anime.serializers import (
    AnimeSerializer,
)
from anime.permissions import (
    AnimePermission,
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

    def create(self, request: DRF_Request) -> DRF_Response:
        """Handles POST-request to show custom_users."""
        ...

    def retrieve(self, request: DRF_Request, pk: int = 0) -> DRF_Response:
        """Handles GET-request with ID to show custom_user."""

        raise APIValidator(
            '\'GET\' метод не имплементирован',
            'warning',
            '403'
        )

    def partial_update(
        self,
        request: DRF_Request,
        pk: int = 0
    ) -> DRF_Response:
        """Handles PATCH-request with ID to show custom_user."""
        ...

    def update(self, request: DRF_Request) -> DRF_Response:
        """Handles PUT-request with ID to show custom_user."""
        ...

    def destroy(self, request: DRF_Request, pk: int = 0) -> DRF_Response:
        """Handles DELETE-request with ID to show custom_user."""
        ...
