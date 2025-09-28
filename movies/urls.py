from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, GenreViewSet, FavoriteMovieViewSet, RecommendationLogViewSet

router = DefaultRouter()
router.register(r"movies", MovieViewSet, basename="movie")
router.register(r"genres", GenreViewSet, basename="genre")
router.register(r"favorites", FavoriteMovieViewSet, basename="favorite")
router.register(r"recommendations", RecommendationLogViewSet, basename="recommendation")

urlpatterns = [
    path("", include(router.urls)),
]
