from django.contrib import admin
from .models import *

# Register your models here.


class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_completed', 'completed_at', 'created_at', 'deadline', 'owner', 'todo_list')
    list_filter = ('name', 'description', 'is_completed', 'completed_at', 'created_at', 'deadline', 'owner', 'todo_list')

class TodoListAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_completed', 'completed_at', 'created_at', 'owner')
    

admin.site.register(TodoItem, TodoItemAdmin)
#admin.site.register(TodoList, TodoListAdmin)