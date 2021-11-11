import scrapy


from FC_scraper.FC_scraper.items import IngredientTypItem


class IngredientTypSpider(scrapy.Spider):
    name = "ingredient_typ"
    start_urls = ['http://przepisy.pl/skladniki/', ]

    def parse(self, response):

        for ingrid in response.css('a.category-tile'):
            item = IngredientTypItem()
            item['name'] = ingrid.css('h2.ng-star-inserted::text').extract_first()
            item.save()
            yield item

            # yield {
            #     'ingridientTypName': ingrid.css('h2.ng-star-inserted::text').get(),
            #     'link_to_ingirdtyp': ingrid.css('a.category-tile::attr(href)').get(),
            # }


class RecipesSpider(scrapy.Spider):
    name = "recipes"
    start_urls = ['https://przepisy.pl/przepisy/dania-i-przekaski/dania-glowne', ]

    def parse(self, response):
        for recipe in response.css('a.recipe-box__title'):
            yield {
                'RecipeName': recipe.css('a.recipe-box__title::text').get(),
                'link_to_recipe': recipe.css('a.recipe-box__title::attr(href)').get(),
            }
