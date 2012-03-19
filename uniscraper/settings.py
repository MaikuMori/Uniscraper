# Scrapy settings for uniscraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'uniscraper'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['uniscraper.spiders']
NEWSPIDER_MODULE = 'uniscraper.spiders'
USER_AGENT = '%s/%s (LU Homework)' % (BOT_NAME, BOT_VERSION)

DEFAULT_ITEM_CLASS = 'uniscraper.items.PlaceItem'

DOWNLOAD_DELAY = '1'

ITEM_PIPELINES = ['uniscraper.pipelines.XmlExportPipeline']