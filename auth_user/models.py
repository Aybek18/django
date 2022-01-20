from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название фильма')
    description = models.TextField(verbose_name='Описание')
    poster = models.BooleanField(default=False)
    year = models.DateField(verbose_name='Дата выхода', default=timezone.now)
    country = models.CharField(verbose_name='Страна', max_length=255)
    dictectory = models.CharField(verbose_name='Режиссер', max_length=255)
    actory = models.ForeignKey('Actor', on_delete=models.CASCADE, related_name='movie_actor')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, related_name='movie_genre')
    world_premiere = models.DateField(verbose_name='Премьера', default=timezone.now)
    budget = models.IntegerField(verbose_name='Бюджет')
    fees_in_country = models.IntegerField(verbose_name='Стоимость')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name='movie_category')
    slug = models.SlugField(unique=True)


class Actor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    age = models.IntegerField(verbose_name="Возраст")
    description = models.TextField(verbose_name="Биография")
    image = models.ImageField(upload_to='actors_photo', verbose_name="Фото профиля")
    slug = models.SlugField(unique=True)


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="Жанр")
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(unique=True)


class MovieImage(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name="Описание")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_image')
    image = models.ImageField(upload_to='movie_image', verbose_name='Кадр из фильма')


class Rating(models.Model):
    star = models.PositiveIntegerField(verbose_name='Оценка',validators=[MinValueValidator(0), MaxValueValidator(10)])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_rating')


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(unique=True)


class Review(models.Model):
    email = models.EmailField(verbose_name='Почта')
    name = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_review')
