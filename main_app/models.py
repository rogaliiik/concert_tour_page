from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(max_length=50)
    verified = models.BooleanField(default=False)


class Concert(models.Model):
    arena = models.CharField(max_length=50)
    date = models.DateField()
    city = models.CharField(max_length=50)