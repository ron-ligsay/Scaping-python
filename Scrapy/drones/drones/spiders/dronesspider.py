import scrapy


class DronesspiderSpider(scrapy.Spider):
    name = "dronesspider"
    allowed_domains = ["jessops.com"]
    start_urls = ["http://jessops.com/"]

    def parse(self, response):
        products = response.css('div.details-pricing')
        for product in products:
            item = {
            'name' : product.css('a::text').get(),
            'price' : product.css('p.price.larger::text').get()
            }
            yield item # return what it finds
        pass
