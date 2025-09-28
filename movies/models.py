from django.conf import settings
from django.db import models


class Movie(models.Model):
    """
    Lightweight Movie model to store only the TMDb movie ID and minimal metadata.
    We only save movies when users interact with them (e.g., mark as favorite).
    """
    tmdb_id = models.PositiveIntegerField(unique=True)
    title = models.CharField(max_length=255)
    poster_path = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class FavoriteMovie(models.Model):
    """
    Stores movies that users mark as favorites.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="favorites"
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="favorited_by"
    )
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "movie")

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"
