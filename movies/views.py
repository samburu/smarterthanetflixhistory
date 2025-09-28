from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics, permissions, status
from .models import Movie, FavoriteMovie
from .serializers import MovieSerializer, FavoriteMovieSerializer
from .services.tmdb import fetch_from_tmdb, TMDbAPIError


# Movies (CRUD optional)
class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all().order_by("-created_at")
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Favorites
class FavoriteMovieListCreateView(generics.ListCreateAPIView):
    serializer_class = FavoriteMovieSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return FavoriteMovie.objects.none()
        return FavoriteMovie.objects.filter(user=self.request.user).select_related("movie")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FavoriteMovieDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = FavoriteMovieSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return FavoriteMovie.objects.none()
        return FavoriteMovie.objects.filter(user=self.request.user).select_related("movie")


class TrendingMoviesView(APIView):
    """
    Get trending movies from TMDb.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            results = fetch_from_tmdb("trending/movie/week")
            return Response(results, status=status.HTTP_200_OK)
        except TMDbAPIError as e:
            return Response({"error": str(e)}, status=status.HTTP_502_BAD_GATEWAY)


class RecommendedMoviesView(APIView):
    """
    Get movie recommendations based on TMDb ID.
    Example: /api/movies/550/recommendations/
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, tmdb_id, *args, **kwargs):
        try:
            results = fetch_from_tmdb(f"movie/{tmdb_id}/recommendations")
            return Response(results, status=status.HTTP_200_OK)
        except TMDbAPIError as e:
            return Response({"error": str(e)}, status=status.HTTP_502_BAD_GATEWAY)
