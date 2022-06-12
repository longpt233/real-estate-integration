import scrapy
from scrapy.selector import Selector
from ..items import CrawlSosanhnhaItem

class BatdongsanSpider(scrapy.Spider):
    i=1
    name = "sosanhnha"
    def start_requests(self):
        start_urls=[
            "https://sosanhnha.com/search?keyword=&iCat=324&iCit=0&iDis=0&price_min=0&price_max=0&page=2"
        ]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        products = response.css('.classifield')
        for product in products:
            link_detail = product.css('.content > a::attr(href)').extract_first()
            yield response.follow(link_detail, self.parse_detail)

        # if self.i < 500:
        #     self.i += 1
        #     path_next = self.base_url + "trang--"+str(self.i)+".html"
        #     yield response.follow(path_next, callback=self.parse)

    def parse_detail(self, response):
        item = CrawlSosanhnhaItem()
        item['title'] = response.css('.detail > .title::text').extract_first()
        # item['description'] = response.css(' ').extract_first()
        item['price'] = response.css('.detail > .detail_top > .box_info > .ct .dt_price').extract_first()
        item['date'] = response.css('.detail > .info > span:last-child::text').extract()
        item['acreage'] = response.css('.detail > .detail_top > .box_info > .ct ').extract_first()
        item['address'] = response.css('.detail > .detail_top > .box_info > .ct > p:last-child > span::text').extract_first()
        # item['user_name'] = response.css().extract_first()
        # item['user_phone'] = response.css().extract_first()
        # item['user_address'] = response.css().extract_first()
        yield item