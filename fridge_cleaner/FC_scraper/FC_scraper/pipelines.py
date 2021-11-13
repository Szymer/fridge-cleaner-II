from itemadapter import ItemAdapter


class FcScraperPipeline:
    def process_item(self, item, spider):
        return item


class IngredientTypPipeline(object):
    def proces_item(self, item, spider):
        item.save()
        return item


class IngredientPipeline(object):
    def proces_item(self, item, spider):
        item.save()
        return item


class RecipePipeline(object):
    def proces_item(self, item, spider):
        item.save()
        return item


class TagPipeline(object):
    def proces_item(self, item, spider):
        item.save()
        return item

class TestPipeline(object):
    def proces_item(self, item, spider):
        item.save()
        return item