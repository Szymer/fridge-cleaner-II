from django.db import models


def typs_from_db():
    query = IngredientTyp.objects.all()
    return query


def typs_pk(typ_name):
    typ = IngredientTyp.objects.get(name=str(typ_name))
    return typ.pk


class Ingredient(models.Model):
    name = models.CharField(max_length=128, unique=True)
    typ = models.ForeignKey("IngredientTyp", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class IngredientTyp(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=516)
    source = models.URLField()
    ingredients = models.ManyToManyField("Ingredient")
    url = models.URLField(unique=True, default=None )
    tags = models.ManyToManyField("tags")


class Tags(models.Model):
    tag_name = models.CharField(max_length=256, unique=True)


class RecipeType(models.Model):
    typ_name = models.CharField(max_length=56, unique=True)
