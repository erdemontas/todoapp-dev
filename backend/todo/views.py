from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from .filters import *

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


class TodoItemView(viewsets.ModelViewSet):
    serializer_class = TodoItemSerializer
    queryset = TodoItem.objects.all()
    

class TodoListView(viewsets.ModelViewSet):
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_class = TodoItemFilter
    
   
