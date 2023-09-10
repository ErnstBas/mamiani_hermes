from django.db import models
from author.model import Author


class Article(models.Model):
    title = models.CharField(max_length=100)  
    text = models.TextField(max_lentgth=1000)
    author = models.ManyToManyField(Author.author)
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to ='images')


    
    
    
