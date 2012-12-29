from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy import log
from scrapy.conf import settings
from googler.items import Page
import re
import googler.utils.loading
#import lxml, lxml.html, lxml.etree, StringIO

class GooglerSpider(CrawlSpider):
    name = 'Googler'

    rules = []
    start_urls = []

    def __init__(self):
        self.queries = settings.get('GOOGLER_QUERIES')
        self.pages_to_get = settings.get('GOOGLER_PAGES_TO_GET_FROM_ENGINE')
        self.engines = googler.utils.loading.load_modules("googler.engines", settings.get('GOOGLER_USE_ENGINES'))
        self.load_crawling_config()
        self.forbid_regexps = map(re.compile, settings.get('GOOGLER_FORBID_URLS'))
        super(GooglerSpider, self).__init__()
#        self.qqq = 1
#    
#    def parse(self, response):
#        log.msg("Downloaded %s" % response.url, log.INFO)
#        with open(str(self.qqq), 'w') as f:
#            content = StringIO.StringIO(response.body)
#            t = lxml.html.parse(content)
#            print >> f, lxml.etree.tostring(t, pretty_print = True)
#        self.qqq += 1
#        return super(GooglerSpider, self).parse(response)
    
    def parse_item(self, response):
        log.msg("Got response on %s" % response.url, log.INFO)
        return self.handle_page(response)

    def parse_found_result(self, new_site_response, engine):
        log.msg("A new site was found %s" % new_site_response.url, log.INFO)
        if any(regex.search(new_site_response.url) for regex in self.forbid_regexps):
            return
        self._rules.extend(Rule(extractor, callback = self.parse_item, follow = True)
                           for extractor in engine.get_link_extractors_for_result(new_site_response.url))
        return self.handle_page(new_site_response)

    def load_crawling_config(self):
        GooglerSpider.start_urls = []
        for eng in self.engines:
            GooglerSpider.start_urls.extend(eng.get_start_pages(self.queries, self.pages_to_get))

        for eng in self.engines:
            GooglerSpider.rules.extend(Rule(extractor,
                                            callback = lambda resp: self.parse_found_result(resp, eng),
                                            follow = True)
                                       for extractor in eng.get_result_extractors())
        
    def handle_page(self, response):
        page = Page()
        page["url"] = response.url
        page["content"] = response.body
        return page
