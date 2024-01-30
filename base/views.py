from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import TodoList

class CreateTodoListItem(CreateView):
     model = TodoList
     fields = ['title', 'description', 'dueDate', 'isComplete']

     def post(self, request):
          return redirect("createnewitem")

