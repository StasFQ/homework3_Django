from django.db import models


class City(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=25)
    offer = models.ManyToManyField(Product)
    actions = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Executor(models.Model):
    city = models.OneToOneField(City, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
