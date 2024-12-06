# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CaipiaoPipeline:

    def open_spider(self, spider):
        """
        一直打开文件
        :param spider:
        :return:
        """
        self.f = open('./双色球.csv', mode='a', encoding='utf-8')

    def process_item(self, item, spider):
        """
        往文件中写数据
        :param item:
        :param spider:
        :return:
        """
        self.f.write(f"{item['qi_hao']}, {'_'.join(item['red_ball'])}, {'_'.join(item['blue_ball'])}\n")

    def close_spider(self, spider):
        """
        直到数据写完，关闭文件
        :param spider:
        :return:
        """
        if self.f:
            self.f.close()
