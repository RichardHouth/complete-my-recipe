from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingred_list = models.TextField(max_length=200)
    instructions = models.TextField(max_length=1000)
    num_ingreds = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.name)

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)