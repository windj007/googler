from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import urllib, urlparse, re
from base_engine import BaseEngine


class Google(BaseEngine):
    _REDIR_URL_RE = re.compile(r'&url=')
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

    def get_link_extractors_for_result(self, found_resource_url):
        parsed_google_res = urlparse.urlparse(found_resource_url)
        if Google._REDIR_URL_RE.search(found_resource_url):
            google_params = urlparse.parse_qs(parsed_google_res.query)
            allowed_domain = urlparse.urlparse(google_params['url']).hostname
        else:
            allowed_domain = parsed_google_res.hostname
        return [SgmlLinkExtractor(allow_domains = [allowed_domain])]