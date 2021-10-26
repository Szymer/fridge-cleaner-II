from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=128, unique=True)
    typ = models.ForeignKey("IngredientTyp", on_delete=models.CASCADE)


class IngredientTyp(models.Model):
    name = models.CharField(max_length=128, unique=True)


class Recipe(models.Model):
    name = models.CharField(max_length=516)
    source = models.ForeignKey("SourceSite", on_delete=models.CASCADE)
    ingredient = models.ManyToManyField("Ingredient")
    rating = models.FloatField(null=True)


class RecipeType(models.Model):
    typ_name = models.CharField(max_length=56, unique=True)


class SourceSite(models.Model):
    name = models.CharField(max_length=128, unique=True)
    url = models.URLField()