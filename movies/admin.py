from django.contrib import admin
from movies.models import Person, Movie, Alias


class AliasInline(admin.StackedInline):
    model = Alias
    extra = 0


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = (
        AliasInline,
    )


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass
