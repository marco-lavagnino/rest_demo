from rest_framework import serializers
from movies.models import Person, Movie


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = (
            'id',
            'last_name',
            'first_name',
            'aliases',
            'starred_movies',
            'directed_movies',
            'produced_movies',
        )


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'id',
            'title',
            'release_year',
            'roman_release_year',
            'actors',
            'directors',
            'producers',
        )
