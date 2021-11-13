from django.db import models


def typs_from_db():
    query = IngredientTyp.objects.all()
    return query


def typs_pk(typ_name):
    typ = IngredientTyp.objects.get(name=str(typ_name))
    return typ.pk


def ingredients_str_list():
    ingredients = Ingredient.objects.all()
    resoult = []
    for ingredient in ingredients:
        resoult.append(ingredient.name)
    return resoult


def tag_str_list():
    tags = Tag.objects.all()
    resoult = []
    for tag in tags:
        resoult.append(tag.name)
    return resoult


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
    url = models.URLField(unique=True, default=None)
    tags = models.ManyToManyField("Tag", null=True)


class Tag(models.Model):
    tag_name = models.CharField(max_length=256, unique=True)


class RecipeType(models.Model):
    typ_name = models.CharField(max_length=56, unique=True)
