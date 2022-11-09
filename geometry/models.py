from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=35)
    email = models.EmailField(max_length=100)


class Logs(models.Model):
    class Method(models.TextChoices):
        POST = 'P', 'POST'
        GET = 'G', 'GET'

    path = models.CharField(max_length=120)
    method = models.CharField(max_length=10, choices=Method.choices)
    time = models.DateTimeField(auto_now_add=True)
