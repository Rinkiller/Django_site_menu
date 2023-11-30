from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterUserForm, CreateRecipesForm
from django.core.files.storage import FileSystemStorage
from .models import Recipes, Category
from .forms import Deep_search

class IndexView(TemplateView):
    template_name = 'menu/index.html'
    def get(self, request):
        recipes = Recipes.objects.all().order_by('-id')[:5]
        return render(request, self.template_name, {'recipes':recipes})

          
class RegisterFormView(generic.CreateView):
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    template_name = 'menu/registration/registration.html' 


class LoginFormView(LoginView):
    form_class = AuthenticationForm
    template_name = 'menu/registration/login.html'
    def get_success_url(self):
        return reverse_lazy('home')

def createRecipes(request):
    message = ""
    if request.method == 'POST':
        form = CreateRecipesForm(request.POST, request.FILES)
        message = "Введенные данные ошибочны"
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            Ingredients = form.cleaned_data['Ingredients']
            cookingSteps = form.cleaned_data['cookingSteps']
            cookingTime = form.cleaned_data['cookingTime']
            image = form.cleaned_data['image']
            nature_of_consumption = form.cleaned_data['nature_of_consumption']
            consistency = form.cleaned_data['consistency']
            feed_temperature = form.cleaned_data['feed_temperature']
            method_of_preparation = form.cleaned_data['method_of_preparation']
            by_appointment = form.cleaned_data['by_appointment']
            recipes = Recipes(name=name, description=description, Ingredients=Ingredients, cookingSteps=cookingSteps, cookingTime=cookingTime, image = image,author=request.user)
            recipes.save()
            fs = FileSystemStorage()
            fs.save(recipes.image.name, recipes.image)
            category = Category(nature_of_consumption=nature_of_consumption, consistency=consistency,feed_temperature=feed_temperature,method_of_preparation=method_of_preparation,by_appointment=by_appointment,nameRecipes=recipes)
            category.save()
            return HttpResponseRedirect('/')
    else:
        form = CreateRecipesForm()
    return render(request, 'menu/createrecipete.html', {'form':form, 'message':message})

def get_recipe(request, id):
    recipte = get_object_or_404(Recipes, pk=id)
    сategory = Category.objects.filter(nameRecipes=recipte.id)[0]
    return render(request, 'menu/get_recipe.html', {'recipte':recipte})

def deep_search(request):
    message = ""
    if request.method == 'POST':
        form = Deep_search(request.POST, request.FILES)
        message = "Введенные данные ошибочны"
        if form.is_valid():
            nature_of_consumption = form.cleaned_data['nature_of_consumption']
            consistency = form.cleaned_data['consistency']
            feed_temperature = form.cleaned_data['feed_temperature']
            method_of_preparation = form.cleaned_data['method_of_preparation']
            by_appointment = form.cleaned_data['by_appointment']
            if not nature_of_consumption and not consistency and not feed_temperature  and not method_of_preparation and not by_appointment:
                message = "Выберите хотябы один пункт"
                form = Deep_search()
                return render(request, 'menu/deep_search.html', {'form':form, 'message':message})
            results =  Category.objects.all()
            if nature_of_consumption:
                results = results.filter(nature_of_consumption=nature_of_consumption)
            if consistency:
                results = results.filter(consistency=consistency)
            if feed_temperature:
                results = results.filter(feed_temperature=feed_temperature)
            if method_of_preparation:
                results = results.filter(method_of_preparation=method_of_preparation)
            if by_appointment:
                results = results.filter(by_appointment=by_appointment)
            reciptes = []
            for rs in results:
                reciptes.append(rs.nameRecipes)
            return render(request, 'menu/get_recipes.html', {'reciptes':reciptes})     
            #return HttpResponseRedirect('/')
    else:
        form = Deep_search()
    return render(request, 'menu/deep_search.html', {'form':form, 'message':message})


def search(request):
    search_query = request.POST.get('search')
    reciptes_all = Recipes.objects.all()
    results = []
    if search_query.lower() == 'все':
        results = Recipes.objects.all()
        return render(request, 'menu/get_recipes.html', {'reciptes':results})
    for rec in reciptes_all:
        if search_query.lower() in rec.name.lower():
            results.append(rec) 
    if not results:
        request.method = 'GET'
        return redirect('deep_search')
    return render(request, 'menu/get_recipes.html', {'reciptes':results})

def editRecipes(request, id): # выбор рецепта для редактирования
    message = ''
    if request.method == 'POST':
        form = CreateRecipesForm(request.POST, request.FILES)
        message = "Введенные данные ошибочны"
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            Ingredients = form.cleaned_data['Ingredients']
            cookingSteps = form.cleaned_data['cookingSteps']
            cookingTime = form.cleaned_data['cookingTime']
            image = form.cleaned_data['image']
            nature_of_consumption = form.cleaned_data['nature_of_consumption']
            consistency = form.cleaned_data['consistency']
            feed_temperature = form.cleaned_data['feed_temperature']
            method_of_preparation = form.cleaned_data['method_of_preparation']
            by_appointment = form.cleaned_data['by_appointment']
            recipe = Recipes.objects.get(pk = id)
            category = Category.objects.get(nameRecipes=recipe)
            recipe.name = name
            recipe.description = description
            recipe.Ingredients = Ingredients
            recipe.cookingSteps = cookingSteps
            recipe.cookingTime = cookingTime
            recipe.image = image
            recipe.save()
            fs = FileSystemStorage()
            fs.save(recipe.image.name, recipe.image)
            category.nature_of_consumption = nature_of_consumption
            category.consistency = consistency
            category.feed_temperature = feed_temperature
            category.method_of_preparation = method_of_preparation
            category.by_appointment = by_appointment
            category.save()
            return HttpResponseRedirect('/')    
    else:
        recipte = Recipes.objects.get(pk = id)
        category = Category.objects.get(nameRecipes=recipte)
        data = {'name':recipte.name,'description':recipte.description,'Ingredients':recipte.Ingredients,'cookingSteps':recipte.cookingSteps,'cookingTime':recipte.cookingTime,'image':recipte.image,'nature_of_consumption':category.nature_of_consumption,'consistency':category.consistency,'feed_temperature':category.feed_temperature,'method_of_preparation':category.method_of_preparation,'by_appointment':category.by_appointment}
        form = CreateRecipesForm(data)
    return render(request, 'menu/edit_recipte.html', {'form':form,'message':message})

def findRecipe(request):
    reciptes = Recipes.objects.filter(author = request.user)
    message = ''
    if not reciptes:
        message = 'У вас нет рецептов. редактировать нечего.'
    return render(request, 'menu/get_edit_recipte.html', {'reciptes':reciptes, 'message':message})
