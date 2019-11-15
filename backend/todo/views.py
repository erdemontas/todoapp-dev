from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import *
from .models import *
import json


class TodoItemView(viewsets.ModelViewSet):
    serializer_class = TodoItemSerializer
    queryset = TodoItem.objects.all()
    
class TodoListView(viewsets.ModelViewSet):
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.all()

    @action(detail=False)
    def show_completed(self, request, pk=None):
        completed_tasks = TodoItem.objects.filter(is_completed=False).values()
        
        print("*****: {}".format(completed_tasks))
        # serializer = self.get_serializer(data=completed_tasks)

        # if serializer.is_valid():
        #     serializer.save()
        #     return Response({"some_ke":"some_value"})
        # else:
        #     return Response(serializer.errors)

        return Response({'status': completed_tasks})
            

    
   
