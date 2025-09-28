from django.urls import path
from . import views

urlpatterns = [
    # Local CRUD
    path("movies/", views.MovieListCreateView.as_view(), name="movie-list"),
    path("movies/<int:pk>/", views.MovieDetailView.as_view(), name="movie-detail"),
    path("favorites/", views.FavoriteMovieListCreateView.as_view(), name="favorite-list"),
    path("favorites/<int:pk>/", views.FavoriteMovieDetailView.as_view(), name="favorite-detail"),

    # TMDb API
    path("trending/", views.TrendingMoviesView.as_view(), name="trending-movies"),
    path("movies/<int:tmdb_id>/recommendations/", views.RecommendedMoviesView.as_view(), name="recommendations"),
]
