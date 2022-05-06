from pyclbr import Class
from django.db import models
from authentication.models import Usuarios

# Create your models here.
"""
class Usuarios(AbstractUser):
    
        Profile user model
    
    email = models.EmailField(max_length=150, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']
    def get_full_name_user(self):
        return {'full_name': f"{self.first_name} {self.last_name}"}
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Usuarios(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    """


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