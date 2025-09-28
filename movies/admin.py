from django.contrib import admin
from .models import Movie, FavoriteMovie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "tmdb_id", "title", "created_at")
    search_fields = ("title", "tmdb_id")
    ordering = ("-created_at",)


@admin.register(FavoriteMovie)
class FavoriteMovieAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "movie", "added_at")
    search_fields = ("user__username", "movie__title")
    ordering = ("-added_at",)
