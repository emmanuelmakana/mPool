import scrapy
import re


class predictz(scrapy.Spider):
    name = "predictz"

    start_urls = [
        'https://www.predictz.com/predictions/'
    ]

    def parse(self, response):
        url = response.url
        page_name = re.search("(?:www\.)(?P<site>.*)(?:\.com|\.co)", url)
        file_name = page_name.group("site")
        with open(file_name, "wb") as f:
            f.write(response.body)

        # yield
