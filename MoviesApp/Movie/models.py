


from operator import mod
from unicodedata import category, name
from django.db import models



class Movies(models.Model):
    image = models.ImageField(upload_to='movies/')
    title = models.CharField(max_length=100)
    descriptions= models.CharField(max_length=500)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} on {self.uploaded_at}'


# Create your models here.
