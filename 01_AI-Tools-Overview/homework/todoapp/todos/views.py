from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
import datetime
from .forms import TodoForm

def todo_list(request):
    todos = Todo.objects.all().order_by('is_completed', 'due_date')
    return render(request, 'todos/todo_list.html', {'todos': todos})

def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('todo_list')
    return render(request, 'todos/todo_form.html', {'form': form})

def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('todo_list')
    return render(request, 'todos/todo_form.html', {'form': form})

def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('todo_list')