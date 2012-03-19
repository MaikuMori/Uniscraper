# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class PlaceItem(Item):
    # define the fields for your item here like:
    # name = Field()
    
    name = Field()
    phone = Field()
    address = Field()
    email = Field()
    branche = Field()
    keywords = Field()
    
    # Google map coordinates.
    lat = Field()
    lon = Field()
