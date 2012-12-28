from scrapy.item import Item, Field

class Page(Item):
    url = Field()
    content = Field()
