from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


nature_of_consumption =['','закуски', 'бутерброды', 'супы', 'основные блюда', 'напитки', 'гарниры', 'соусы', 'сладкие блюда', 'десерты', 'коктейли и др. смешанные напитки с содержанием алкоголя', 'мучные кулинарные изделия', 'скомплектованные завтраки', 'обеды', 'ужины']
consistency =['','жидкие', 'полужидкие', 'густые', 'пюреобразные', 'мягкие', 'вязкие', 'рассыпчатые']
feed_temperature =['','холодные', 'горячие', 'охлажденные', 'замороженные']
method_of_preparation =['','маринованные', 'квашеные', 'отварные', 'припущенные', 'тушеные', 'жареные (основным способом, во фритюре, гриль и др.)', 'пассерованные', 'бланшированные', 'запеченные', 'печеные', 'фламбированные', 'ИК-нагрев', 'СВЧ-обработка' ]
by_appointment = ['','общего назначения', 'для диетического', 'лечебного', 'школьного', 'детского питания', 'вегетарианские', 'для специального питания']




class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label = 'Логин', widget = forms.TextInput(attrs={'class':'form-input'}))
    email = forms.EmailField(label = 'Email', widget = forms.EmailInput(attrs={'class':'form-input'}))
    password1 = forms.CharField(label = 'Пароль', widget = forms.PasswordInput(attrs={'class':'form-input'}))
    password2 = forms.CharField(label = 'Повтор пароля', widget = forms.PasswordInput(attrs={'class':'form-input'}))
    
    class Meta:
        model = User
        fields = {'username','email','password1','password2'}

class CreateRecipesForm(forms.Form):
    name = forms.CharField(max_length=50, label='Название рецепта')
    description = forms.CharField(label='Описание рецепта', widget=forms.Textarea)
    Ingredients = forms.CharField(label='Ингридиенты', widget=forms.Textarea)
    cookingSteps = forms.CharField(label='Шаги приготовления', widget=forms.Textarea)
    cookingTime = forms.CharField(max_length=20,label='Время приготовления')
    image = forms.ImageField(label='Изображение блюда')
    nature_of_consumption = forms.ChoiceField(label = 'По характеру потребления', choices  = [(cons,cons) for cons in nature_of_consumption])
    consistency = forms.ChoiceField(label = 'По консистенции', choices  = [(consisten,consisten) for consisten in consistency])
    feed_temperature = forms.ChoiceField(label = 'По температуре подачи', choices  = [(temp,temp) for temp in feed_temperature]) 
    method_of_preparation = forms.ChoiceField(label = 'По способу приготовления', choices  = [(method,method) for method in method_of_preparation]) 
    by_appointment = forms.ChoiceField(label = 'По назначению', choices  = [(appointment,appointment) for appointment in by_appointment]) 


class Deep_search(forms.Form):
    nature_of_consumption = forms.ChoiceField(label = 'По характеру потребления', choices  = [(cons,cons) for cons in nature_of_consumption], required=False)
    consistency = forms.ChoiceField(label = 'По консистенции', choices  = [(consisten,consisten) for consisten in consistency], required=False)
    feed_temperature = forms.ChoiceField(label = 'По температуре подачи', choices  = [(temp,temp) for temp in feed_temperature], required=False) 
    method_of_preparation = forms.ChoiceField(label = 'По способу приготовления', choices  = [(method,method) for method in method_of_preparation], required=False) 
    by_appointment = forms.ChoiceField(label = 'По назначению', choices  = [(appointment,appointment) for appointment in by_appointment], required=False) 