from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import urllib
from base_engine import BaseEngine


class Google(BaseEngine):
    def get_result_extractors(self):
        return [
                SgmlLinkExtractor(allow_domains = ["google.ru", "google.com"],
                                  restrict_xpaths = '//h3[@class="r"]'
                                  ),
                ]

    def make_pages_for_query(self, query, num_of_pages):
        encoded_query = urllib.urlencode({'q': query})
        result = ["http://www.google.com/search?%s&source=hp&btnG=%s&gbv=1" % \
                  (encoded_query, "%CF%EE%E8%F1%EA+%E2+Google")]
        for page in range(1, num_of_pages):
            result.append("http://www.google.com/search?%s&newwindow=1&gbv=1&ie=UTF-8&prmd=ivns&start=%d&sa=N" % \
                          (encoded_query, 10*page))
        return result
