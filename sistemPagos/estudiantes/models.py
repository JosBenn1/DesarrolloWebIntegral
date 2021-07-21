from django.db import models

class Estudiante(models.Model):
    image = models.ImageField()
    matricula = models.IntegerField()
    name = models.TextField()
    lastname = models.TextField()
    email = models.EmailField()
    password = models.TextField()   
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)