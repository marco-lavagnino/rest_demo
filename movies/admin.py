from django.contrib import admin
from movies.models import Person, Movie, Alias


class AliasInline(admin.StackedInline):
    model = Alias


class PersonInline(admin.StackedInline):
    model = Person


class MovieInline(admin.StackedInline):
    model = Movie


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass
