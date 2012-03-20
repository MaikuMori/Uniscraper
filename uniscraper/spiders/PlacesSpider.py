# -*- coding: utf-8 -*-

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy.utils.url import urljoin_rfc
from scrapy.utils.response import get_base_url


from uniscraper.items import PlaceItem

class PlacesSpider(BaseSpider):
    name = "PlacesSpider"
    
    allowed_domains = ["www.1188.lv"]
    
    # By default get only fuel stations.
    start_urls = (
        'http://www.1188.lv/katalogs/Degvielas%20uzpildes%20stacijas',
        )

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        
        stations = hxs.select("//div[@id='SearchResults']/div[contains(@class, 'Item')]")
        for station in stations:
            item = PlaceItem()
            
            # Get the "Col-1" div and extra data from that.
            col1 = station.select("div[@class='Col-1']")
            item["Name"] = col1.select("h2[@class='Title']/a[contains(@href, 'katalogs')]/text()").extract()[0]
            item["Branche"] = col1.select("p[@class='Branche']/a/text()").extract()[0]
            # Check if there are keywords.
            if col1.select("p[@class='KeywordExcerpt']"):
                infos = station.select(".//div[@class='Description']/p")
                for info in infos:
                    info_b = info.select("b/text()").extract()
                    if info_b and (info_b[0] == u"Atslēgas vārdi:"):
                        item["Keywords"] = info.select("text()").extract()[1].strip().split(", ")
            
            # Get the "Col-2" div and extra data from that.
            col2 = station.select("div[@class='Col-2']")
            contacts = col2.select("ul[@class='Contacts']")
            if contacts:
                # Check if the item has phone number field.
                phone = contacts.select("li[@class='IconPhone']/text()").extract()
                if phone:
                    item["Phone"] = phone[0]
                # Check if the item has email field.
                email = contacts.select("li[@class='IconMail']/a/@href").extract()
                if email:
                    item["Email"] = email[0][7:]
            
            item["Address"] = col2.select("p[@class='IconPlace3']/a/text()").extract()[0]

            # Get the map data.
            gmap = station.select(".//div[contains(@id, 'map_')]")
            if gmap:
                item["Lat"] = gmap.select("@data-g-coord-x").extract()[0].strip()
                item["Lon"] = gmap.select("@data-g-coord-y").extract()[0].strip()

            yield item 
        
        # Add the rest of the pages to the page pool.
        for url in hxs.select("//a[contains(@href, '?page=')]/@href").extract():
            # Build full url from relative one.
            url = urljoin_rfc(get_base_url(response), url)
            yield Request(url, callback=self.parse)
