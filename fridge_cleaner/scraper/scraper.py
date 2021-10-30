
from spatula import (
    HtmlPage, HtmlListPage, CSS, XPath, SelectorError
)

#
# class IngridientTypeList(HtmlListPage):
#     source = "https://www.przepisy.pl/skladniki"
#
#     selector = CSS(".ng-star-inserted h2")
#
#     def process_item(self, item):
#         typ_name = item.getchildren()
#         return dict(
#             typ_name=typ_name.text,
#
#         )


class IngridientTypeList(HtmlPage):
    source = "https://www.przepisy.pl/skladniki"
    def process_page(self):
        marital_status = CSS("h2",num_items=16).match(self.root)

        # children = CSS("#children").match_one(self.root)
        # hired = CSS("#hired").match_one(self.root)
        for item in marital_status:
            award = CSS("h2").match_one(item).text
        return dict(
            marital_status=marital_status.text

             # children=children.text,
            # hired=hired.text,
            # self.input is the data passed in from the prior scrape,
            # in this case a dict we can expand here
            **self.input,
        )