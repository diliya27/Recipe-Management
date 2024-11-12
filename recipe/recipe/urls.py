
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from management import views

from rest_framework.authtoken import views as rviews

router=SimpleRouter()
router.register('recipe',views.RecipeView)
router.register('review',views.ReviewView)
router.register('register',views.UserView)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),

path('login', rviews.obtain_auth_token),
path('search',views.SearchView.as_view()),
path('searchingredient',views. SearchIngredient.as_view()),
path('searchmeal',views.SearchMeal.as_view()),
path('searchcuisine',views.SearchCuisine.as_view()),
    path('Reviewfilter/<int:pk>',views.Reviewfilter.as_view()),


path('logout',views.LogoutAPIView.as_view())  #logoutview


]
