from django.urls import path, include
from .views import (LandingPageAPIView, ArtistAPIView, AlbomAPIView, ArtistDetailsAPIView,
                    AlbomDetailAPIView, SongAPIViewSet)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("songs", SongAPIViewSet)

urlpatterns = [
    path('landing/', LandingPageAPIView.as_view(), name="landing"),
    path('artists/', ArtistAPIView.as_view(), name="artists"),
    path('artists/<int:id>', ArtistDetailsAPIView.as_view(), name="artist-detail"),
    path('alboms/', AlbomAPIView.as_view(), name="alboms"),
    path('alboms/<int:id>', AlbomDetailAPIView.as_view(), name="alboms-detail"),
    path('', include(router.urls))
]

