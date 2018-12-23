from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from rest_framework.compat import MaxValueValidator, MinValueValidator


class Author(models.Model):
     name=models.CharField(max_length=250)
     designation=models.CharField(max_length=250)

     def __str__(self):
         return self.name

class Category(models.Model):
     title=models.CharField(max_length=250)

     def __str__(self):
         return self.title




class Article(models.Model):
     title=models.CharField(max_length=250)
     description =models.TextField()
     author=models.ForeignKey(Author,on_delete=models.CASCADE)
     category=models.ForeignKey(Category,on_delete=models.CASCADE)
     created=models.DateTimeField()
     published=models.BooleanField(default=True)
     views=models.IntegerField(default=0)



     def __str__(self):
         return self.title


