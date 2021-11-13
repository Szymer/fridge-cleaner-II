import scrapy
from unidecode import unidecode

from FC_scraper.FC_scraper.items import IngredientTypItem, IngredientItem, RecipeItem, TagItem, AddIngToRecipe
from fridge_cleaner_app.models import typs_from_db, IngredientTyp, ingredients_str_list, tag_str_list, \
    Recipe, Ingredient


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



class TagsSpider(scrapy.Spider, ):
    name = "  tags spider"
    typs = typs_from_db()
    urls = []

    for typ in typs:
        name = typ.name.lower()
        name = unidecode(name).replace(" ", "-")
        number_of_pages = 5
        for page in range(number_of_pages):
            urls.append(f'http://przepisy.pl/skladniki/{name}?page={page}')

    start_urls = urls

    def parse(self, response, **kwargs):
        for tag in response.css('span.tags-title'):
            item = TagItem()
            item['name'] = tag.css('a.tags-item::text').get()
            item.save()
            yield item


### scraping recipes


class RecipeTagsSpider(scrapy.Spider):
    name = " Recipe tags spider"

    def __init__(self, url=None, *args, **kwargs):
        super(RecipeTagsSpider, self).__init__(*args, **kwargs)
        self.start_urls = [f'{url}']

    def parse(self, response, **kwargs):
        recipes_tag_list = []
        for tag in response.css('span.tags-title'):
            ingredient = tag.css('a.tags-item::text').get()
            if tag in tag_str_list():
                recipes_tag_list.append(ingredient)
        return recipes_tag_list


class RecipesSpider(scrapy.Spider):
    name = "recipes"
    typs = typs_from_db()
    urls = []

    for typ in typs:
        name = typ.name.lower()
        name = unidecode(name).replace(" ", "-")
        number_of_pages = 99
        for page in range(number_of_pages):
            urls.append(f'http://przepisy.pl/skladniki/{name}?page={page}')

    start_urls = urls

    def parse(self, response):
        for recipe in response.css('a.recipe-box__title'):
            url = recipe.css('a.recipe-box__title::attr(href)').get()
            item = RecipeItem()
            item['source'] = "Przepisy.pl"  # hardkodowane źródło bo nie ma innych
            item['name'] = recipe.css('a.recipe-box__title::text').extract_first()
            item['url'] = url
            # ings = RecipeDetailsSpider.parse(url=url)
            # for x in ings:
            #
            # # item['tags'] = ...
            item.save()
            yield item


class RecipeDetailsSpider(scrapy.Spider):
    name = " Recipe detail spider"
    recipes = Recipe.objects.all()
    urls = []
    for recipe in recipes:
        urls.append(f'http://przepisy.pl{recipe.url}')

    start_urls = urls

    def add_ing(self, ing, title):

        ing2 = ing.strip()
        ing2 = ing2.capitalize()
        print(title, "ing2:", ing2)

        recipe = Recipe.objects.get(name=title)

        if ing2 in ingredients_str_list():
            ingirdnet_instance = Ingredient.objects.get(name=ing2)
            recipe.ingredients.add(ingirdnet_instance)
            recipe.save()



    def parse(self, response, **kwargs):
        title = response.css('h1.title::text').get(),
        for ing in response.css('div.ingredients-list-content-item'):
            ingrid = ing.css('span.text-bg-white::text').get(),
            # title = ing.css('h1.title::text').get(),
            self.add_ing(ingrid[0], title[0])




