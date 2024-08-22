# todos/urls.py
from django.urls import path
from .views import todo_list, edit_todo, delete_todo, toggle_complete

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('edit/<int:pk>/', edit_todo, name='edit_todo'),
    path('delete/<int:pk>/', delete_todo, name='delete_todo'),
    path('toggle_complete/<int:pk>/', toggle_complete, name='toggle_complete'),
]
