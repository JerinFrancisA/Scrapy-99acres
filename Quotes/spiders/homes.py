import scrapy
from ..items import QuotesItem


class Spider(scrapy.Spider):
    name = "homes"
    pno = 60
    start_urls = ["https://www.99acres.com/rent-property-in-bangalore-east-ffid-page-6"]

    def parse(self, response):
        items = QuotesItem()

        all_div_houses = response.css("div.oldSrp")
        for houses in all_div_houses:
            p = houses.css(".margin\:0::text").extract()
            t = houses.css("a::text").extract()
            l = houses.css(".srpttl a").xpath("@href").extract()
            a = houses.css(".topActions+ span b::text").extract()
            s = houses.css(".doElip b::text").extract()
            d = houses.css(".wBr > span::text").extract()
            f = houses.css(".fcInit i").xpath("@value").extract()

            if p != []:
                price = p[0].strip()
            else:
                price = ''

            if t != []:
                title = t[0].strip()
            else:
                title = ''

            if a != []:
                area = a[0].strip()
            else:
                area = ''

            if s != []:
                society = s[0].strip()
            else:
                society = ''

            if l != []:
                link = l[0].strip()
            else:
                link = ''

            features = ''
            for i in f:
                features = features + i + ", "
            features = features[:len(features) - 2]

            description = ''
            for i in d:
                if i != '... ':
                    description += i

            items["price"] = price
            items["title"] = title
            items["link"] = link
            items["area"] = area
            items["society"] = society
            items["description"] = description
            items["features"] = features

            yield items

        next_page = "https://www.99acres.com/rent-property-in-bangalore-east-ffid-page-"+str(Spider.pno)
        if Spider.pno <= 262:
            Spider.pno += 1
            yield response.follow(next_page, callback = self.parse)