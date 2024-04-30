from rest_framework import serializers
from .models import Artist, Albom, Songs


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("name", "image")   # "__all__" barchasini oladi


class AlbomSerializer(serializers.ModelSerializer):

    artist = ArtistSerializer()

    class Meta:
        model = Albom
        fields = ("title", "artist", "cover")


class SongSerializer(serializers.ModelSerializer):

    albom = AlbomSerializer()

    class Meta:
        model = Songs
        fields = ("title", "cover", "albom")

