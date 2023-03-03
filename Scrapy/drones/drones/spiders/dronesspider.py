import scrapy


class DronesspiderSpider(scrapy.Spider):
    name = "dronesspider"
    allowed_domains = ["jessops.com"]
    start_urls = ["http://jessops.com/"]

    def parse(self, response):
        pass
