from django.db import models


# Create your models here.ha
class Ingredient(models.Model):
    name: models.CharField(max_length=128, unique=True)
    typ: models.ForeignKey("IngredientTyp")


class IngredientTyp(models.Model):
    name: models.CharField(max_length=128, unique=True)


class Recipe(models.Model):
    name: models.CharField(max_length=516)
    source: models.ForeignKey("SourceSite")
    ingredient: models.ManyToManyField("Ingredient")


class RecipeType(models.Model):
    typ_name: models.CharField(max_length=56, unique=True)

class SourceSite(models.Model):
    name: models.CharField(max_length=128, unique=True)
    url: models.URLField()

