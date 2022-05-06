from pyclbr import Class
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

"""class Usuarios(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)"""

class Usuarios(AbstractUser):
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['password']

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Priority(models.Model):
    priorityName = models.CharField(max_length=50)

    def __str__(self):
        return self.priorityName

class Tareas(models.Model):
    id_tarea = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    dead_line = models.DateField()
    description = models.CharField(max_length=50)
    isCompleted = models.BooleanField()
    priority_id = models.ForeignKey(Priority, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Usuarios, on_delete=models.CASCADE)