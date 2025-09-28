from rest_framework import serializers
from .models import Movie, FavoriteMovie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "tmdb_id", "title", "poster_path", "created_at"]


class FavoriteMovieSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    movie_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = FavoriteMovie
        fields = ["id", "user", "movie", "movie_id", "added_at"]
        read_only_fields = ["id", "user", "movie", "added_at"]

    def create(self, validated_data):
        user = self.context["request"].user
        tmdb_id = validated_data.pop("movie_id")

        movie, _ = Movie.objects.get_or_create(
            tmdb_id=tmdb_id,
            defaults={"title": validated_data.get("title", f"TMDb {tmdb_id}")},
        )
        favorite, created = FavoriteMovie.objects.get_or_create(user=user, movie=movie)
        return favorite
