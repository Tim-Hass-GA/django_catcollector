from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cat(models.Model):
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    age = models.IntegerField()
    # toys = models.ManyToManyField(Toy)

    def __str__(self):
        return self.name

class Toy(models.Model):
    name = models.CharField(max_length=100)
    cats = models.ManyToManyField(Cat)

    def __str__(self):
        return self.name
