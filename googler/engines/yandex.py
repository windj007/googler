from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import urllib
from base_engine import BaseEngine


class Yandex(BaseEngine):
    def get_result_extractors(self):
        return [
                SgmlLinkExtractor(allow_domains = ["yandex.ru"],
                                  restrict_xpaths = '//div[@class="b-body-items"]'
                                  )
                ]

    def make_pages_for_query(self, query, num_of_pages):
        encoded_query = urllib.urlencode(query)
        result = ["http://yandex.ru/yandsearch?text=%s&lr=213" % encoded_query]
        for page in range(1, num_of_pages):
            result.append("http://yandex.ru/yandsearch?text=%s&lr=213&p=%d" % \
                          (encoded_query, page))
        return result
