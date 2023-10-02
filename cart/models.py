from django.db import models
from django.contrib.contenttypes.models import ContentType
from main.models import Books
from accounts.models import CustomUser

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, null=True, blank=True,  on_delete=models.CASCADE)
    name = models.CharField(Books, max_length=100)
    price = models.DecimalField(Books, max_digits=10, decimal_places=2)
    image = models.ImageField(Books,)

    def __str__(self):
        return str(self.id)

    def get_cart_items(self):
        return self.Books.all()

