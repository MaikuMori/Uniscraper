# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class PlaceItem(Item):
    # define the fields for your item here like:
    # name = Field()
    
    # Required.
    Name = Field()
    Branche = Field()
    Address = Field()
   
    # Optional.

    # Google map coordinates.
    Lat = Field()
    Lon = Field()
    
    Email = Field()
    Phone = Field()
    
    Keywords = Field()