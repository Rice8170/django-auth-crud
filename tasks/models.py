from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title =models.CharField(max_length=100)
    description = models.TextField(blank=True)
    # Si no se pasa el dato el framework le pasa la hora en el la que fue creado 
    created = models.DateField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    user =  models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + '- by ' + self.user.username

