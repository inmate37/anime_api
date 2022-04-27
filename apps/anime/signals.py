from django.db.models.signals import (
    pre_save,
    post_save,
)
from django.dispatch import receiver

from anime.models import Anime


@receiver(
    pre_save,
    sender=Anime
)
def post_save_anime(
    sender: Anime,
    instance: Anime,
    created: bool,
    **kwargs: dict
) -> None:
    """Signal post-save Anime."""
    ...


@receiver(
    post_save,
    sender=Anime
)
def pre_save_anime(
    sender: Anime,
    instance: Anime,
    created: bool,
    **kwargs: dict
) -> None:
    """Signal pre-save Anime."""
    ...
