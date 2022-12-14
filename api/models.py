from django.db import models


class Location(models.Model):
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name


class Item(models.Model):
    trade_code = models.CharField(max_length=150)
    date = models.DateField(default=None)
    high = models.FloatField(default=None)
    low = models.FloatField(default=None)
    open = models.FloatField(default=None)
    close = models.FloatField(default=None)
    volume = models.FloatField(default=None)

    

    def __str__(self):
        return self.trade_code