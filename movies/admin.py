from django.contrib import admin
from .models import User, Movie, Genre, FavoriteMovie, RecommendationLog


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "date_joined", "last_login")
    search_fields = ("username", "email")


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "tmdb_id", "release_date", "created_at")
    search_fields = ("title",)
    list_filter = ("release_date",)
    filter_horizontal = ("genres",)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(FavoriteMovie)
class FavoriteMovieAdmin(admin.ModelAdmin):
    list_display = ("user", "movie", "created_at")
    list_filter = ("created_at",)


@admin.register(RecommendationLog)
class RecommendationLogAdmin(admin.ModelAdmin):
    list_display = ("user", "movie", "reason", "recommended_at")
    list_filter = ("reason", "recommended_at")
