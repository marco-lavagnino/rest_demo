from django.db import models
from numeral import int2roman


class Alias(models.Model):
    name = models.CharField(max_length=50)
    person = models.ForeignKey(
        'Person',
        on_delete=models.CASCADE,
        related_name='aliases',
    )

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Movie(models.Model):
    title = models.CharField(max_length=50)
    release_year = models.IntegerField()

    actors = models.ManyToManyField(
        'Person',
        related_name='starred_movies',
    )

    directors = models.ManyToManyField(
        'Person',
        related_name='directed_movies',
    )

    producers = models.ManyToManyField(
        'Person',
        related_name='produced_movies',
    )

    def __str__(self):
        return "{} ({})".format(self.title, self.release_year)

    def roman_representation(self):
        return int2roman(self.release_year, only_ascii=True)
