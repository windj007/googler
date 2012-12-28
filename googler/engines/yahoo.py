from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import urllib
from base_engine import BaseEngine


class Yahoo(BaseEngine):
    def get_result_extractors(self):
        return [
                SgmlLinkExtractor(allow_domains = ["yahoo.com"],
                                  restrict_xpaths = '//div[@id="web"]'
                                  )
                ]

    def make_pages_for_query(self, query, num_of_pages):
        encoded_query = urllib.urlencode(query)
        result = ["http://ru.search.yahoo.com/search?p=%s&toggle=1&cop=mss&ei=UTF-8&fr=yfp-t-722" % encoded_query]
        for page in range(1, num_of_pages):
            result.append("http://ru.search.yahoo.com/search?p=%s&ei=UTF-8&fr=yfp-t-722&xargs=0&pstart=1&b=%d" % \
                          (encoded_query, 10*page + 1))
        return result