from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(max_length=50)
    verified = models.BooleanField(default=False)


class Concert(models.Model):
    arena = models.CharField(max_length=50)
    date = models.DateField()
    city = models.CharField(max_length=50)


class Merch(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField(default=20)
    image = models.ImageField(null=True, blank=True, upload_to='images/')

