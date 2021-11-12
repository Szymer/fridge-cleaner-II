import scrapy

from FC_scraper.FC_scraper.items import IngredientTypItem, IngredientItem
from fridge_cleaner_app.models import typs_from_db, typs_pk


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
        urls.append(f'http://przepisy.pl/skladniki/{typ.name.lower()}')

    start_urls = urls

    def parse(self, response):
        item = IngredientItem()
        item['typ'] = typs_pk(response.css('li.span.ng-star-inserted::text').extract_first())
        for ingrid in response.css('a.category-tile'):
            item['name'] = ingrid.css('h2.ng-star-inserted::text').extract_first()
            item.save()
            yield item


class RecipesSpider(scrapy.Spider):
    name = "recipes"
    start_urls = ['https://przepisy.pl/przepisy/dania-i-przekaski/dania-glowne', ]

    def parse(self, response):
        for recipe in response.css('a.recipe-box__title'):
            yield {
                'RecipeName': recipe.css('a.recipe-box__title::text').get(),
                'link_to_recipe': recipe.css('a.recipe-box__title::attr(href)').get(),
            }
