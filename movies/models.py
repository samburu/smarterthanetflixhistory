import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Extend the default Django user for authentication.
    We keep AbstractUser to inherit username, email, password, etc.
    """
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Genre(models.Model):
    """
    Movie genre (e.g., Action, Drama).
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    """
    Movie data sourced from TMDb API.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tmdb_id = models.PositiveIntegerField(unique=True)  # external reference
    title = models.CharField(max_length=255)
    overview = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    poster_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    genres = models.ManyToManyField(Genre, related_name="movies")

    def __str__(self):
        return self.title


class FavoriteMovie(models.Model):
    """
    Mapping of users to their favorite movies.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="favorited_by")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "movie")  # prevent duplicate favorites

    def __str__(self):
        return f"{self.user.username} ♥ {self.movie.title}"


class RecommendationLog(models.Model):
    """
    Log of movies recommended to users for audit/debug purposes.
    """
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="recommendations")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="recommendations")
    recommended_at = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Recommended {self.movie.title} to {self.user or 'anonymous'} ({self.reason})"
