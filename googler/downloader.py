import re
from scrapy.exceptions import IgnoreRequest


class FilteringDownloader(object):
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings['GOOGLER_ALLOWED_MIME'])
    
    def __init__(self, mime_regexs):
        self.regexps = map(re.compile, mime_regexs)
    
    def process_response(self, request, response, spider):
        if 'Content-Type' in response.headers: 
            mime = response.headers['Content-Type']
            if any(regex.search(mime) for regex in self.regexps):
                return response
            else:
                raise IgnoreRequest("mime %s is not allowed" % mime)
        raise IgnoreRequest("mime is not specified")
