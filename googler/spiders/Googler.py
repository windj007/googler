#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy import log
from scrapy.conf import settings
from googler.items import Page
import itertools
import googler.utils.loading


class GooglerSpider(CrawlSpider):
    name = 'Googler'

    rules = []
    start_urls = []

    def __init__(self):
        self.queries = settings.get('GOOGLER_QUERIES')
        self.pages_to_get = settings.get('GOOGLER_PAGES_TO_GET_FROM_ENGINE')
        GooglerSpider.start_urls = itertools.chain(eng.get_start_pages(self.queries, self.pages_to_get)
                                                   for eng in self.engines)
        self.engines = googler.utils.loading.load_modules("googler.engines", settings.get('GOOGLER_USE_ENGINES'))
        self.load_rules()
        super(GooglerSpider, self).__init__()
    
    def parse_item(self, response):
        log.msg("Got response on %s" % response.url, log.INFO)
        return self.handle_page(response)

    def parse_found_result(self, new_site_response):
        log.msg("A new site was found %s" % new_site_response.url, log.INFO)
        return self.handle_page(new_site_response)

    def load_rules(self):
        for eng in self.engines:
            GooglerSpider.rules.extend(Rule(extractor,
                                            callback = 'parse_found_result',
                                            follow = True)
                                       for extractor in eng.get_result_extractors())
#        GooglerSpider.rules.append(Rule(SgmlLinkExtractor(),
#                                        callback = 'parse_item',
#                                        follow = True ) )

    def handle_page(self, response):
        page = Page()
        page["url"] = response.url
        page["content"] = response.body
        return page
