# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from scrapy.contrib.exporter import XmlItemExporter

from xml.sax.xmlreader import AttributesImpl


# We'll add our own namespace to the xml document so have to modify the exporter a bit.
# TODO:Should be in a different file.
class XmlPlacesExporter(XmlItemExporter):
    
    def start_exporting(self):
        self.xg.startDocument()
        self.xg.startElement(self.root_element, AttributesImpl({"xmlns": "UniscraperPlaces"}))

class XmlExportPipeline(object):

    def __init__(self):
        # Defines exported fields and order in which should appear.
        self.fields_to_export = [
            "Name",
            "Branche",
            "Address",
            "Lat", "Lon",
            "Email",
            "Phone",
            "Keywords"
        ]
        # Register the signal handlers.
        dispatcher.connect(self.spider_opened, signals.spider_opened)
        dispatcher.connect(self.spider_closed, signals.spider_closed)
        self.files = {}

    def spider_opened(self, spider):
        xml_file = open('%s_results.xml' % spider.name, 'w+b')
        self.files[spider] = xml_file
        self.exporter = XmlPlacesExporter(xml_file, item_element = "Place", root_element = "Places",
                                          fields_to_export = self.fields_to_export)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        xml_file = self.files.pop(spider)
        xml_file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item