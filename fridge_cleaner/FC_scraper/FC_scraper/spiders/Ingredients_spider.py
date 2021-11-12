import scrapy
from unidecode import unidecode

from FC_scraper.FC_scraper.items import IngredientTypItem, IngredientItem
from fridge_cleaner_app.models import typs_from_db, typs_pk, IngredientTyp


class IngredientTypSpider(scrapy.Spider):
    name = "ingredient_typ"
    start_urls = ['http://przepisy.pl/skladniki/', ]

    def parse(self, response):
        for ingrid in response.css('a.category-tile'):
            item = IngredientTypItem()
            item['name'] = ingrid.css('h2.ng-star-inserted::text').extract_first()
            item.save()
            yield item


class IngredientSpider(scrapy.Spider):
    name = 'ingredient'
    typs = typs_from_db()
    urls = []

    for typ in typs:
        name = typ.name.lower()
        name = unidecode(name).replace(" ", "-")

        urls.append(f'http://przepisy.pl/skladniki/{name}')

    start_urls = urls

    def parse(self, response):

        typ_name_css = response.css('span.ng-star-inserted::text').get()
        typ = IngredientTyp.objects.get(name=typ_name_css)

        if response.css('a.category-tile'):
            for ingrid in response.css('a.category-tile'):
                item = IngredientItem()
                item['typ'] = typ
                item['name'] = ingrid.css('h2.ng-star-inserted::text').get()
                item.save()
                yield item
        else:
            item = IngredientItem()
            item['typ'] = typ
            item['name'] = typ_name_css
            item.save()
            yield item


class RecipesSpider(scrapy.Spider):
    name = "recipes"
    typs = typs_from_db()
    urls = []

    for typ in typs:
        name = typ.name.lower()
        name = unidecode(name).replace(" ", "-")
        number_of_pages =

        urls.append(f'http://przepisy.pl/skladniki/{name}')

    start_urls = urls

    def parse(self, response):
        for recipe in response.css('a.recipe-box__title'):
            yield {
                'RecipeName': recipe.css('a.recipe-box__title::text').get(),
                'link_to_recipe': recipe.css('a.recipe-box__title::attr(href)').get(),
            }

