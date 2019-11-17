from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .serializers import *
from .models import *





class TodoItemView(viewsets.ModelViewSet):
    serializer_class = TodoItemSerializer
   
    
    def  get_queryset(self):
         queryset = TodoItem.objects.filter(owner=self.request.user)
         return queryset

    @action(detail=False)
    def show_completed(self, request, pk=None):
        completed_tasks = TodoItem.objects.filter(owner=self.request.user, is_completed=False)
        serializer = TodoItemSerializer(completed_tasks, many=True)
        data= serializer.data
        return Response(data)
    
    @action(detail=False)
    def show_expired(self, request, pk=None):
        expired_tasks = TodoItem.objects.filter(owner=self.request.user, is_completed=False)
        expired_tasks = expired_tasks.filter(deadline__date= datetime.now())
        serializer = TodoItemSerializer(expired_tasks, many=True)
        data= serializer.data
        return Response(data)
   
    def perform_update(self, serializer):
        serializer.save()
    
class TodoListView(viewsets.ModelViewSet):
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.all()
    
    def  get_queryset(self):
         queryset = TodoItem.objects.filter(owner=self.request.user)
         return queryset


def SignupView(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('register')
 
    else:
        f = UserCreationForm()
 
    return render(request, 'signup.html', {'form': f})


@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

