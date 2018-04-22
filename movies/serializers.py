from rest_framework import serializers
from movies.models import Person, Movie, Alias


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    aliases = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=Alias.objects.all(),
    )

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
