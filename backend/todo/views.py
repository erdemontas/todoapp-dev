from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import *
from .models import *
#from .filters import *

class TodoItemView(viewsets.ModelViewSet):
    serializer_class = TodoItemSerializer
    queryset = TodoItem.objects.all()
    
class TodoListView(viewsets.ModelViewSet):
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.all()

    @action(detail=False)
    def show_completed(self, request, pk=None):
        completed_tasks = TodoItem.objects.all().filter(is_completed=False)
        print(completed_tasks)
        page = self.paginate_queryset(completed_tasks)

        if page is not None:
            serializer = self.get_serializer(completed_tasks, many=True)
            return Response(serializer.data)

    
   
