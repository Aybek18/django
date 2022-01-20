from rest_framework import permissions
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from auth_user.models import (Product, Movie, Review, Category, Actor, Rating, Genre, MovieImage)
from auth_user.serializers import (ProductSerializer, MovieSerializer, RatingSerializer, ReviewSerializer,
                                   CategorySerializer, ActorSerializer, MovieImageSerializer, GenreSerializer)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'head']
    permission_classes = [permissions.AllowAny]


class CreateProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['post', 'create']
    permission_classes = [permissions.IsAuthenticated]


class CreateMovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    http_method_names = ['post', 'create']
    permission_classes = [permissions.IsAuthenticated]


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    http_method_names = ['get', 'head']
    permission_classes = [permissions.AllowAny]


class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    http_method_names = ['get', 'head']
    permission_classes = [permissions.AllowAny]


class CreateRatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    http_method_names = ['post', 'create']
    permission_classes = [permissions.IsAuthenticated]


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    http_method_names = ['get', 'head']
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]


class CreateReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    http_method_names = ['post', 'create']
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    http_method_names = ['get', 'head']
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class CreateCategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    http_method_names = ['post', 'create']
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    http_method_names = ['get', 'head']
    permission_classes = [permissions.AllowAny]


class CreateActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    http_method_names = ['post', 'create']
    permission_classes = [permissions.IsAuthenticated]


class MovieImageViewSet(ModelViewSet):
    queryset = MovieImage.objects.all()
    serializer_class = MovieImageSerializer
    http_method_names = ['get', 'head']
    permission_classes = [permissions.AllowAny]


class CreateMovieImageViewSet(ModelViewSet):
    queryset = MovieImage.objects.all()
    serializer_class = MovieImageSerializer
    http_method_names = ['post', 'create']
    permission_classes = [permissions.IsAuthenticated]


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    http_method_names = ['get', 'head']
    permission_classes = [permissions.AllowAny]


class CreateGenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    http_method_names = ['post', 'create']
    permission_classes = [permissions.IsAuthenticated]

# from django.db.models import Q
# from rest_framework import permissions
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from drf_yasg.utils import swagger_auto_schema
# from django.utils.decorators import method_decorator
#
# from .serializers import PostSerializer, LikeSerializer
# from .models import Post, Like


# class MyQ(Q):
#     default = 'OR'
#
#
# @method_decorator(name='post', decorator=swagger_auto_schema(operation_summary='Этот API 😅😁'))
# @method_decorator(name='get', decorator=swagger_auto_schema(operation_summary='Этот API 😅😁'))
# class PostLisCreateAPIView(ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [permissions.AllowAny, ]
#
#
# @method_decorator(name='post', decorator=swagger_auto_schema(operation_summary='Этот API 😅😁'))
# @method_decorator(name='get', decorator=swagger_auto_schema(operation_summary='Этот API 😅😁'))
# class LikeLisCreateAPIView(ListCreateAPIView):
#     queryset = Like.objects.all()
#     serializer_class = LikeSerializer
#     permission_classes = [permissions.AllowAny, ]
