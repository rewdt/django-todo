from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import forms
from .models import Todos

# Create your views here.

def alltodos(request):
    if(request.method == 'POST'):
        form = forms.CreateForm(request.POST)
        if form.is_valid():
            # title = form.cleaned_data['title'],
            # description = form.cleaned_data['description'],
            # start_time = form.cleaned_data['start_time'],
            # todos = Todos(title=title, description=description, start_time=start_time)
            form.save()
            return HttpResponseRedirect('/todos/')
        else:
            print('invalid')

    context = {'createForm': forms.CreateForm}
    return render(request, 'todos/addtodos.html', context)

def todolist(request):
    todos = Todos.objects.all()
    context = {'todos': todos}
    return render(request, 'todos/todolist.html', context)
