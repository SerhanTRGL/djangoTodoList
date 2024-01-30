from django.db import models

# Create your models here.


class TodoList(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    startDate = models.DateTimeField(auto_now_add=True)
    dueDate = models.DateTimeField(null=True)
    itemID = models.BigAutoField(primary_key=True)
    isComplete = models.BooleanField(default=False)
