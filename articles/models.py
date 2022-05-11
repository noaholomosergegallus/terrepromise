from email.mime import image
from importlib.resources import contents
from turtle import title
from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=120)

    def __str__(self) :
        return self.name
    




class Articles(models.Model):

     title=models.CharField(max_length=100)
     content=models.TextField()
     image=models.ImageField()
     category=models.ForeignKey(Category,on_delete=models.CASCADE)
     created_at=models.DateTimeField(auto_now_add=True)
     updated_at=models.DateTimeField(auto_now=True)

     def __str__(self) :
        return self.title