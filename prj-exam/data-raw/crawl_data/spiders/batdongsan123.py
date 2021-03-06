import scrapy
from scrapy.selector import Selector
from ..items import CrawlBatdongsan123

class BatdongsanSpider(scrapy.Spider):
    i=1
    name = "bds123"
    base_url="https://bds123.vn/ban-can-ho-chung-cu.html?page="
    def start_requests(self):
        start_urls=[
            "https://bds123.vn/ban-can-ho-chung-cu.html"
        ]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        products = response.css('article')
        for product in products:
            link_detail = product.css('a::attr(href)').extract_first()
            yield response.follow(link_detail, self.parse_detail)

        if self.i < 500:
            self.i += 1
            path_next = self.base_url +str(self.i)
            yield response.follow(path_next, callback=self.parse)

    def parse_detail(self, response):
        item = CrawlBatdongsan123()
        item['title'] = response.css('.leftCol .post-header > h1::text').extract_first()
        item['description'] = response.css('.leftCol > .section:nth-child(1) > div > p::text').extract()
        item['link_image'] = response.css('.the-post > .post-images > .image-item > img::attr(data-src)').extract_first()
        item['url_page'] = response.request.url
        item['price'] = response.css('.leftCol .post-header > .post-features > .post-price::text').extract() + response.css('.leftCol .post-header > .post-features > .post-price > i::text').extract()
        item['bedroom'] = response.css('.leftCol .post-header > .post-features > .post-bedroom::text').extract()
        item['bathroom'] = response.css('.leftCol .post-header > .post-features > .post-bathroom::text').extract()
        item['acreage'] = response.css('.leftCol .post-header > .post-features > .post-acreage::text').extract()
        item['address'] = response.css('.leftCol .post-header > .post-features > p> span::text').extract_first()
        item['direction'] = response.css('.leftCol .post-header > .post-features > .post-direction::text').extract()
        item['code'] = response.css('.leftCol .table-wrap > table > tbody > tr:nth-child(1) > td:nth-child(2)::text').extract_first()
        item['date'] = response.css('.leftCol .table-wrap > table > tbody > tr:nth-child(5) > td:nth-child(2) time::text').extract_first()
        item['name_contact'] = response.css('.rightCol > .aside-box > .aside-box-content > a  .author-name::text').extract_first()
        item['project'] = response.css('.leftCol .table-wrap > table > tbody > tr:nth-child(3) > td:nth-child(2)::text').extract_first()
        item['phone_contact'] = response.css('.rightCol > .aside-box-author > .aside-box-content .btn-phone::text').extract()
        yield item



