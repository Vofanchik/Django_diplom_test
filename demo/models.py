from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=50)
    state = models.BooleanField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
