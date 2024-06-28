import scrapy
from scrapy.http import Request
from crawldata.items import CrawldataItem

class PostSpider(scrapy.Spider):
    name = "post"
    allowed_domains = ["duhocsunny.edu.vn"]
    start_urls = ['https://duhocsunny.edu.vn/bai-viet/']

    def parse(self, response):
        # Lấy danh sách các bài viết
        articles = response.xpath('//div[@class="col bg-white post-card col-span-4 md:col-span-1"]')
        for article in articles:
            item = CrawldataItem()
            item['title'] = article.xpath('.//div[1]/h3/a/text()').get()
            item['link'] = response.urljoin(article.xpath('.//div[1]/h3/a/@href').get())
            item['image_urls'] = [response.urljoin(article.xpath('.//a/img/@src').get())]
            item['summary'] = article.xpath('.//div[1]/div/p/text()').get()
            
            # Gửi yêu cầu để crawl nội dung chi tiết của từng bài viết
            yield Request(item['link'], callback=self.parse_article, meta={'item': item})

    def parse_article(self, response):
        # Lấy nội dung chi tiết của bài viết từ response
        item = response.meta['item']
        # Cập nhật các trường thông tin chi tiết của bài viết
        item['content'] = response.xpath('//div[@class="wprt-container"]/p/span/text()').getall()
        # Các trường thông tin khác bạn muốn lấy từ trang chi tiết có thể được thêm vào đây
        
        yield item
