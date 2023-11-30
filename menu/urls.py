
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.IndexView.as_view(), name="home"),
    path('register/', views.RegisterFormView.as_view(), name="register"),
    path('login/', views.LoginFormView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('createRecipes/', views.createRecipes, name="createRecipes"),
    path('recipe/<int:id>/', views.get_recipe, name='get_recipe'),
    path('search/recipe/<int:id>/', views.get_recipe, name='get_recipe'),
    path('deep_search/recipe/<int:id>/', views.get_recipe, name='get_recipe'),
    path('search/', views.search, name='search'),
    path('deep_search/', views.deep_search, name='deep_search'),
    path('findRecipe/', views.findRecipe, name='findRecipe'),
    path('findRecipe/editRecipes/<int:id>/', views.editRecipes, name='editRecipes'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
