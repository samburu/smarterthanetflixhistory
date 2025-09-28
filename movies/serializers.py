from rest_framework import serializers
from .models import User, Movie, Genre, FavoriteMovie, RecommendationLog


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ["id", "tmdb_id", "title", "overview", "release_date", "poster_url", "created_at", "genres"]


class FavoriteMovieSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    movie_id = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all(), source="movie", write_only=True
    )

    class Meta:
        model = FavoriteMovie
        fields = ["id", "user", "movie", "movie_id", "created_at"]
        read_only_fields = ["user"]

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


class RecommendationLogSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = RecommendationLog
        fields = ["id", "user", "movie", "recommended_at", "reason"]
