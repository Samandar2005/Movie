from django.db import models
from datetime import date

from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to="static/images/actors/")

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100, default='')
    description = models.TextField()
    poster = models.ImageField(upload_to="static/images/movies")
    year = models.PositiveSmallIntegerField(default=2019)
    country = models.CharField(max_length=30)
    directors = models.ManyToManyField(
        Actor, related_name="film_director")
    actors = models.ManyToManyField(
        Actor, related_name="film_actor")
    genres = models.ManyToManyField(Genre)
    world_premiere = models.DateField(default=date.today)
    budget = models.PositiveIntegerField(
        "Бюджет", default=0)
    fees_in_usa = models.PositiveIntegerField(
        "Сборы в США", default=0
    )
    fess_in_world = models.PositiveIntegerField(
        "Сборы в мире", default=0
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=130, unique=True)
    trailer = models.FileField(
        upload_to='static/videos/trailer', blank=True, null=True)
    movies = models.FileField(
        upload_to='static/videos/movies', blank=True, null=True)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})


class MovieShots(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="static/images/movie_shots/")
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class RatingStar(models.Model):
    value = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.value


class Rating(models.Model):
    ip = models.CharField(max_length=15)
    star = models.ForeignKey(
        RatingStar, on_delete=models.CASCADE)
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.star} - {self.movie}"


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=5000)
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, blank=True, null=True
    )
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"
