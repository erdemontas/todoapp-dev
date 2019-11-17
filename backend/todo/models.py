from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class TodoList(models.Model):
    name = models.CharField(max_length=200, default="blank title")
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(default=datetime.now(), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    class Meta:
        verbose_name = "Todo List"
        verbose_name_plural = "Todo Lists"
        ordering = ["name","created_at", "is_completed", ]
        
    def __str__(self):
            return self.name


class TodoItem(models.Model):
    name = models.CharField(max_length=200, default="blank title")
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, null=False)
    description = models.TextField(max_length=200, default="Blank text")
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(default=datetime.now(), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(default=datetime.now(), null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    previous_item = models.IntegerField(default=0)


    class Meta:
        verbose_name = "Todo Item"
        verbose_name_plural = "Todo Item"
        ordering = ["id","created_at", "is_completed","deadline","name" ]

    def __str__(self):
            return self.name


