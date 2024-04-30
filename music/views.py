from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artist, Albom, Songs
from .serializers import ArtistSerializer, AlbomSerializer, SongSerializer


class LandingPageAPIView(APIView):
    def get(self, request):
        return Response(data={"message: 'Hi lazy devaloper'"})

    def post(self, request):
        return Response(data={"message: 'Post request this is'"})


class ArtistAPIView(APIView):
    def get(self, request):
        artists = Artist.objects.all()
        serializers = ArtistSerializer(artists, many=True)
        return Response(data=serializers.data)


class AlbomAPIView(APIView):
    def get(self, request):
        alboms = Albom.objects.all()
        serializers = AlbomSerializer(alboms, many=True)
        return Response(data=serializers.data)


class SongAPIView(APIView):
    def get(self, request):
        songs = Songs.objects.all()
        serializers = SongSerializer(songs, many=True)
        return Response(data=serializers.data)

