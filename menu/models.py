from django.db import models
# Create your models here.
from django.contrib.auth.models import User
# Рецепты:
# ○ Название
# ○ Описание
# ○ Шаги приготовления
# ○ Время приготовления
# ○ Изображение
# ○ Автор
# ○ *другие поля на ваш выбор, например ингредиенты и т.п.
class Recipes(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    Ingredients = models.TextField() 
    cookingSteps = models.TextField()
    cookingTime = models.CharField(max_length=20)
    image = models.ImageField(upload_to='cooking_image/')
    author = models.ForeignKey(User, verbose_name='Автор', db_column='author', related_name='author', max_length=30,on_delete=models.PROTECT)
    def __str__(self) -> str:
        return f'Рецепт:{self.name} Автор:{self.author}'
    
# Категории рецептов
# ○ Название
# ○ *другие поля на ваш выбор
class Category(models.Model):
    nature_of_consumption = models.CharField(max_length=20) # по характеру потребления (закуски, супы, напитки, каша, выпечка);
    consistency = models.CharField(max_length=20)   # по консистенции (жидкие, густые, вязкие и т.д.);
    feed_temperature = models.CharField(max_length=20)  #по температуре подачи (холодные, горячие, охлаждённые, замороженные);
    method_of_preparation = models.CharField(max_length=20) #по способу приготовления (жареные, тушёные, запечённые, отварные);
    by_appointment = models.CharField(max_length=20)    # по назначению (для детского, диетического питания и др.)
    nameRecipes = models.ForeignKey(Recipes, on_delete=models.PROTECT)
    def __str__(self) -> str:
        return f'по характеру потребления:{self.nature_of_consumption}  consistency:{self.consistency}  nameRecipes:{self.nameRecipes}'
    