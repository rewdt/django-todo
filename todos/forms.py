from django import forms
from django.utils import timezone
from .models import Todos

class CreateForm(forms.ModelForm):
    class Meta:
        model = Todos
        fields = ['title', 'description', 'start_time']
        widgets = {
            'title' : forms.TextInput(), 
            'description' : forms.TextInput(), 
            'start_time' : forms.SelectDateWidget(),
            }