# todos/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import ToDo
from .forms import ToDoForm  # We will create this form next

def todo_list(request):
    todos = ToDo.objects.all()
    return render(request, 'todos/todo_list.html', {'todos': todos})

def edit_todo(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = ToDoForm(instance=todo)
    return render(request, 'todos/edit_todo.html', {'form': form})

def delete_todo(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todos/todo_list.html')

def toggle_complete(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo_list')
