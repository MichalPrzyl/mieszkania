from django.db import models

class Apartment(models.Model):
    name = models.CharField(max_length=100, unique=True)
    link = models.CharField(max_length=255, unique=True)

class PriceRecord(models.Model):
    apartment = models.ForeignKey('mieszkania.Apartment', models.CASCADE)
    price = models.IntegerField()
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)