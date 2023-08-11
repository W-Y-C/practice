import scrapy
from downloadnovel.items import DownloadfictionItem
from downloadnovel.items import styleoffictionItem


class QimaoSpider(scrapy.Spider):
    name = "qimao"
    allowed_domains = ["qimao.com"]
    start_urls = ["https://qimao.com"]

    def parse(self, response):
        temp = response.css(
            '#__layout > div > header > div.qm-header.index-header > div.qm-header-menu.white > div > div > div.left-col > ul > li:nth-child(2) > a::attr(href)').extract_first()
        new_url = response.urljoin(temp)

        # 调用解析方法去解析新的URL
        yield scrapy.Request(new_url, callback=self.parsenewpage)

    def parsenewpage(self, response):
        threeDiv = response.xpath('/html/body/div[3]/div/div[1]/ul/li[2]/div[2]/div')
        for div in threeDiv:
            a_list = div.xpath('./a')
            for a in a_list:
                # 类型的链接
                urlOfdifferentTypenovel = response.urljoin(a.xpath('./@href').get())
                # 小说类型(现代言情,古代言情.......)
                NameofdifferentNovel = a.xpath('./text()').get()

                # 实例化Item对象，并保存数据
                item1 = DownloadfictionItem()
                item1['urlOfdifferentTypenovel'] = urlOfdifferentTypenovel
                item1['NameofdifferentNovel'] = NameofdifferentNovel

                # 将Item对象返回，交给后续的Item Pipeline处理,用以保存到数据库
                if item1 is not None:
                    yield item1

                # 跳转到每一个单独的小说类型再去深度爬取(比如我们第一个跳转到 全部 这个类型的小说页面中去
                # ,类似的还有 现代言情,古代言情等.....)
                yield scrapy.Request(urlOfdifferentTypenovel, callback=self.parse_another_page,
                                     meta={'param1': urlOfdifferentTypenovel, 'param2': NameofdifferentNovel})

    # 跳转到具体类型的小说再进行深度爬取(比如我们第一次跳转到全部这个类型的小说中实现爬取)
    def parse_another_page(self, response):
        # 以参数的形式,获取小说的类型
        # style=response.meta.get('param2')
        # 在一个具体类型的小说页面中,页面的下方有很多展现出来的小说都被一个一个li包裹着
        li_list = response.xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[1]/ul/li')
        for li in li_list:
            # 具体小说的超链接(比如偷偷藏不住,斗破苍穹的跳转地址等等)
            urlOfnovel = response.urljoin(li.xpath('./div[1]/a/@href').get()).strip()
            # 具体小说封面地址的超链接(用来后面做前后端交互使用)
            coverofnovelurl=li.xpath('./div[1]/a/img/@src').get().strip()
            # 具体小说名称(比如偷偷藏不住,斗破苍穹)
            nameOfnovel = li.xpath('./div[2]/span[1]/a/text()').get().strip()
            # 具体小说的标签(比如霸道总裁等等)
            tagOfnovel = li.xpath('./div[2]/span[2]/em/text()').get().strip()
            # 具体小说的状态(比如连载中,完结等等)
            stateOfnovel = li.xpath('./div[2]/span[2]/text()').get().strip()
            # 具体小说简介
            briefintroductionOfnovel = li.xpath('./div[2]/span[3]/text()').get().strip()
            # 具体小说作者及最后更新时间
            authorOfnovel = li.xpath('./div[2]/p/span/text()').get().strip()
            # print("*"*100)

            # 实例化Item对象，并保存数据
            item2 = styleoffictionItem()
            # 以参数的形式,获取小说的类型
            item2['style'] = response.meta.get('param2')
            item2['coverofnovelurl'] = coverofnovelurl
            item2['urlOfnovel'] = urlOfnovel
            item2['nameOfnovel'] = nameOfnovel
            item2['tagOfnovel'] = tagOfnovel
            item2['stateOfnovel'] = stateOfnovel
            item2['briefintroductionOfnovel'] = briefintroductionOfnovel
            item2['authorOfnovel'] = authorOfnovel

            # 打印小说封面地址
            # print(coverofnovelurl)

            # 将Item对象返回，交给后续的Item Pipeline处理,用以保存到数据库
            if item2 is not None:
                yield item2

        # 处理解析得到的数据，或者继续生成新的URL并调用对应的解析方法
        # ...
        # 如果需要继续解析新的URL，可以继续使用yield scrapy.Request()方法
        # 并指定一个回调函数来处理新的请求的响应
        # yield scrapy.Request(another_url, callback=self.parse_another_page)
