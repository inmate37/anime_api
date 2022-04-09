from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

# from django.db.models import QuerySet

from auths.models import CustomUser


class ListUsers(APIView):
    """
    View for CustomUser.

    * Does-not require token authentication.
    * Only superusers are able to access this view.
    """
    permission_classes: tuple = (
        permissions.IsAdminUser,
    )

    def get(self, request: Request) -> Response:
        """Return list of all users."""

        data: list = [
            user.password for user in CustomUser.objects.all()
        ]
        return Response(data)
