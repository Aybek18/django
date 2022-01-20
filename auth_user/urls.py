from rest_framework.routers import DefaultRouter
from auth_user.views import *

router = DefaultRouter()
router.register('api/v1/get/product', ProductViewSet, basename='get_product'),
router.register('api/v1/create/product', CreateProductViewSet, basename='create_product'),
router.register('api/v1/create/movie',  CreateMovieViewSet, basename='create_movie'),
router.register('api/v1/get/movie',  MovieViewSet, basename='get_movie'),
router.register('api/v1/get/movie-image', MovieImageViewSet, basename='get_movie_image'),
router.register('api/v1/create/movie-image', CreateMovieImageViewSet, basename='create_movie_image'),
router.register('api/v1/get/actor', ActorViewSet, basename='get_actor'),
router.register('api/v1/create/actor', CreateActorViewSet, basename='create_actor'),
router.register('api/v1/get/genre', GenreViewSet, basename='get_genre'),
router.register('api/v1/create/genre', CreateGenreViewSet, basename='create_genre'),
router.register('api/v1/create/category', CreateCategoryViewSet, basename='create_category'),
router.register('api/v1/get/category', CategoryViewSet, basename='get_actor'),
router.register('api/v1/create/rating', CreateRatingViewSet, basename='create_rating'),
router.register('api/v1/get/rating', RatingViewSet, basename='get_rating'),
router.register('api/v1/create/review', CreateReviewViewSet, basename='create_review'),
router.register('api/v1/get/review', ReviewViewSet, basename='get_review'),



urlpatterns = router.urls
