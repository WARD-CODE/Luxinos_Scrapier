import scrapy
import json
from unicodedata import normalize
from ..items import LuxItem

class LuxBookspiderSpider(scrapy.Spider):
    name = 'lux_bookspider'
    allowed_domains = ['sreality.cz']
    start_urls = ['http://sreality.cz/']
    
    def start_requests(self):
        url = f"https://www.sreality.cz/api/en/v2/estates?category_main_cb=1&category_type_cb=1&sort=0&per_page=500"
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response, **kwargs):
        jsonfile = json.loads(response.body)
        for item in jsonfile["_embedded"]["estates"]:
            flat = LuxItem()
            flat["name"] = normalize('NFKD', item['name'])
            flat["img_url"] = item["_links"]["images"][0]["href"]

            yield flat
        
        