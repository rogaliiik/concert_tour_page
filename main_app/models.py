from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(max_length=50)
    verified = models.BooleanField(default=False)
