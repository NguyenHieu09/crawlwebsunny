from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

class CrawldataPipeline:
    def process_item(self, item, spider):
        return item

class CustomImagesPipeline(ImagesPipeline):

    def item_completed(self, results, item, info):
        # Lấy danh sách các hình ảnh đã được tải xuống thành công
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        
        # Không lưu trường `image_paths` vào item
        return item
