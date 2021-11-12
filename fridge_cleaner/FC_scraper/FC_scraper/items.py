# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
# from scrapy.contrib.djangoitem import DjangoItem
from fridge_cleaner_app.models import Recipe, IngredientTyp, Ingredient


class FcScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class RecipeItem(DjangoItem):
    django_model = Recipe
    name = scrapy.Field(defoult="no name")


class IngredientTypItem(DjangoItem):
    django_model = IngredientTyp


class IngredientItem(DjangoItem):
    django_model = Ingredient
