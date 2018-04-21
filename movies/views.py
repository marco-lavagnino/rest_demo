from rest_framework import routers, viewsets
from movies.serializers import PersonSerializer, MovieSerializer
from movies.models import Person, Movie


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


router = routers.DefaultRouter()
router.register(r'people', PersonViewSet)
router.register(r'movies', MovieViewSet)
