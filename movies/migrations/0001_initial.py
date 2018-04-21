# Generated by Django 2.0.4 on 2018-04-21 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('release_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='starred_movies', to='movies.Person'),
        ),
        migrations.AddField(
            model_name='movie',
            name='directors',
            field=models.ManyToManyField(related_name='directed_movies', to='movies.Person'),
        ),
        migrations.AddField(
            model_name='movie',
            name='producers',
            field=models.ManyToManyField(related_name='produced_movies', to='movies.Person'),
        ),
        migrations.AddField(
            model_name='alias',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aliases', to='movies.Person'),
        ),
    ]
