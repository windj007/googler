from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import urlparse

class BaseEngine(object):
    def get_result_extractors(self):
        return []

    def get_start_pages(self, queries, num_of_pages):
        result = []
        for query in queries:
            result.extend(self.make_pages_for_query(query, num_of_pages))
        return result

    def make_pages_for_query(self, query, num_of_pages):
        return []
    
    def get_link_extractors_for_result(self, found_resource_url):
        parsed = urlparse.urlparse(found_resource_url)
        return [SgmlLinkExtractor(allow = [parsed.hostname],
                                  allow_domains = [parsed.hostname])]