from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item, Field
from bs4 import BeautifulSoup
import requests


def get_sitemap(url):
    get_url = requests.get(url)

    if get_url.status_code == 200:
        return get_url.text
    else:
        print('Unable to fetch sitemap: %s.' % url)

def process_sitemap(s):
    soup = BeautifulSoup(s)
    result = []

    for loc in soup.findAll('loc'):
        result.append(loc.text)

    return result

class MyItems(Item):
    referer =Field()
    response= Field()
    status = Field()

class MySpider(CrawlSpider):
    name = "test-crawler"
    sitemap = get_sitemap('https://developers.cloudflare.com/sitemap.xml')
    sitemap_links = process_sitemap(sitemap)
    gateway_links = [ x for x in sitemap_links if "/gateway" in x ]
    target_domains = ["developers.cloudflare.com"]
    start_urls = gateway_links
    handle_httpstatus_list = [404, 410, 301, 500]

    custom_settings = {
        'CONCURRENT_REQUESTS': 2,
        'DOWNLOAD_DELAY': 0.5
    }

    rules = (
        Rule(LinkExtractor(allow_domains=target_domains), callback='parse_my_url', follow=False),
    )

    def parse_my_url(self, response):
        if response.status in [404,410,301,500]:
              item = MyItems()
              item['referer'] = response.request.headers.get('Referer', None)
              item['status'] = response.status
              item['response']= response.url
              yield item
        yield None