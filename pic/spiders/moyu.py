import scrapy
from pic.items import PicItem


class MoyuSpider(scrapy.Spider):
    name = "moyu"
    allowed_domains = ["www.moyublog.com"]
    start_urls = ["https://www.moyublog.com/hdwallpapers/fengjing/"]

    def parse(self, response, **kwargs):
        li_list = response.xpath("//div[@class='slist']/ul/li")

        for li in li_list:
            href_list = li.xpath("./a/@href").extract_first()
            # src_name = li.xpath("./a/b/text()").extract_first()
            # print(src_url, src_name)
            # break
            yield scrapy.Request(href_list, callback=self.parse_details)

    def parse_details(self, response, **kwargs):
        pic = PicItem()
        img_src = response.xpath("//div[@class='photo-pic']/p/img/@src").extract_first()
        img_name = response.xpath("//div[@class='photo-pic']/p/img/@alt").extract_first()
        pic['src_name'] = img_name
        pic['src_url'] = img_src
        # print(type(img_name))
        yield pic  # 返回一个item对象
