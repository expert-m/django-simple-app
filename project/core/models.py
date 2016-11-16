from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=255)
    regions = models.ManyToManyField(Region)

    def __str__(self):
        return self.name


class Provider(models.Model):
    name = models.CharField(max_length=255)
    regions = models.ManyToManyField(Region)

    def __str__(self):
        return self.name
