import scrapy
from scrapy_djangoitem import DjangoItem

from fridge_cleaner_app.models import Recipe, IngredientTyp, Ingredient, Tag


class FcScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class RecipeItem(DjangoItem):
    django_model = Recipe


class IngredientTypItem(DjangoItem):
    django_model = IngredientTyp


class IngredientItem(DjangoItem):
    django_model = Ingredient


class TagItem(DjangoItem):
    django_model = Tag


class AddIngToRecipe(scrapy.Item):
    ingredient = scrapy.Field()
    title = scrapy.Field()
