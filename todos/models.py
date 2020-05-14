from django.db import models

# Create your models here.

class Todos(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()