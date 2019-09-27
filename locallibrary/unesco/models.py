from django.db import models

# Create your models here.
class Category(models.Model) :
    name = models.CharField(max_length=128,null=True)

    def __str__(self) :
        return self.name

class States(models.Model) :
    name = models.CharField(max_length=128,null=True)

    def __str__(self) :
        return self.name

class Region(models.Model) :
    name = models.CharField(max_length=128,null=True)

    def __str__(self) :
        return self.name

class Iso(models.Model) :
    name = models.CharField(max_length=128,null=True)

    def __str__(self) :
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    description = models.CharField(max_length=128,null=True)
    justification = models.CharField(max_length=128,null=True)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    area_hectares = models.FloatField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    states = models.ForeignKey(States, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE)

    def __str__(self) :
        return self.name
