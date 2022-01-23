from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2048)


class Offers(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
