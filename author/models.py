from django.db import models

class Author(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    bio = models.TextField(max_lentgth=1000)
    image = models.ImageField()
    email = models.EmailField()
    
    
