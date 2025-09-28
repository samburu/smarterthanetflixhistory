from rest_framework import viewsets, permissions
from .models import Movie, Genre, FavoriteMovie, RecommendationLog
from .serializers import MovieSerializer, GenreSerializer, FavoriteMovieSerializer, RecommendationLogSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FavoriteMovieViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteMovieSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FavoriteMovie.objects.filter(user=self.request.user)


class RecommendationLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RecommendationLog.objects.all().select_related("movie", "user")
    serializer_class = RecommendationLogSerializer
    permission_classes = [permissions.IsAdminUser]
