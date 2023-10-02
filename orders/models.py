from django.db import models
from main.models import Books
from  accounts.models import CustomUser
# Create your models here.


class Order(models.Model):
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return '{}'.format(self.id)