from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import urllib
from base_engine import BaseEngine


class Bing(BaseEngine):
    def get_result_extractors(self):
        return [
                SgmlLinkExtractor(restrict_xpaths = '//div[@class="sb_tlst"]')
                ]
    
    def make_pages_for_query(self, query, num_of_pages):
        encoded_query = urllib.urlencode({'q': query})
        result = ["http://www.bing.com/search?%s&go=&qs=ns&filt=all&form=QBLH" % encoded_query]
        for page in range(1, num_of_pages):
            result.append("http://www.bing.com/search?%s&go=&qs=ns&filt=all&form=PERE%s&first=%d" % \
                          (encoded_query, str(page) if page > 1 else "", 10*page + 1))
        return result
