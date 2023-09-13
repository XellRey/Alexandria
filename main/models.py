from django.db import models

# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    about = models.CharField(max_length=1000)
    photo = models.ImageField(upload_to="uploads-")
    count = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()
    file = models.FileField(null=True,blank=True)