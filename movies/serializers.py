from rest_framework import serializers
from movies.models import Person, Movie, Alias


class AliasSlugRelatedField(serializers.SlugRelatedField):

    def to_internal_value(self, data):
        try:
            alias, created = self.get_queryset().get_or_create(name=data, person=None)
            return alias
        except (TypeError, ValueError):
            self.fail('invalid')


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    aliases = AliasSlugRelatedField(
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
