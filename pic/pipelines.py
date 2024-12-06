# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
from scrapy.pipelines.images import ImagesPipeline


class PicPipeline:
    def process_item(self, item, spider):
        return item


class FengJingBiZhi(ImagesPipeline):

    def get_media_requests(self, item, info):
        yield scrapy.Request(item['src_url'], meta={"src_name": item['src_name']})

    def file_path(self, request, response=None, info=None, *, item=None):
        file_name = request.url.split('/')[-1]
        dir_name = request.meta['src_name']
        return f"{dir_name}/{file_name}"
        # return request.meta['src_name']
        # return super().file_path(request, response, info, item=item)

    def item_completed(self, results, item, info):
        print(results)


