from django.core.management.base import BaseCommand

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from FC_scraper.FC_scraper.spiders.Ingredients_spider import RecipesSpider


class Command(BaseCommand):
    help = "get all recipes "

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())

        process.crawl(RecipesSpider)
        process.start()



