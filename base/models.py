from django.db import models

# Create your models here.

class TodoList(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    startDate = models.DateTimeField()
    itemID = models.BigAutoField(primary_key=True)
