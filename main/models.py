from django.db import models
from accounts.models import CustomUser
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

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.subject
