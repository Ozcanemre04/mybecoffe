






from django import forms
from django.forms import  ModelForm
from .models import recettes, users


from django.contrib.auth.forms import UserCreationForm
from django import forms






class recettesForm(ModelForm):
    date=forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}))
    class Meta:
        model=recettes
        fields=['date','recette']
        





class registerForm(UserCreationForm):
    class Meta:
        model=users
        fields=['username','email','last_name','first_name','chef']
        


