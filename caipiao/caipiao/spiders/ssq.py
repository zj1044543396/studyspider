import scrapy
from caipiao.items import CaipiaoItem


class SsqSpider(scrapy.Spider):
    name = "ssq"
    # allowed_domains = ["datachart.500.com"]
    start_urls = ["https://datachart.500.com/dlt/"]

    def parse(self, response, **kwargs):
        # print(response.text)
        # tr索引从第三个开始
        tr_list = response.xpath("//table[@id='chartsTable']/tr[position()>2]")
        cp = CaipiaoItem()
        for tr in tr_list:
            # qihao = tr.xpath("./td[1]/text()").extract_first()
            # print(qihao)
            qi_hao = tr.css('td[align="center"]::text').get()  # 期号
            red_ball = tr.css(".chartBall01::text").getall()  # 红球号码
            blue_ball = tr.css(".chartBall02::text").getall()
            if qi_hao is None:
                continue
            if qi_hao.startswith("2"):
                # print(qihao, red_ball, blue_ball)
                cp['qi_hao'] = qi_hao
                cp['red_ball'] = red_ball
                cp['blue_ball'] = blue_ball
            yield cp
