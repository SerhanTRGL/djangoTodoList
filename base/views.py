from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import TodoList


class TodoListView(ListView):
     model = TodoList
     template_name = "home.html"
     context_object_name = "todo_list_items"


class CreateTodoListItem(CreateView):
     model = TodoList
     fields = ['title', 'description', 'dueDate', 'isComplete']
     template_name = "create_new_item.html"
     success_url = reverse_lazy('home')

class UpdateTodoListItem(UpdateView):
     model = TodoList

     fields = ['title', 'description', 'dueDate', 'isComplete']
     template_name = "update_item.html"
     success_url = reverse_lazy('home')

class DeleteTodoListItem(DeleteView):
     model = TodoList
     template_name = "delete_item.html"
     context_object_name = "todo_item"
     success_url = reverse_lazy('home')

class ViewAllItems(ListView):
     model = TodoList
     template_name = "view_all_items.html"
     context_object_name = "todo_list_items"