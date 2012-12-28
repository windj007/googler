from scrapy import log 
import os
import hashlib

class GooglerPipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings['GOOGLER_OUTPUT_DIRECTORY'])
    
    def __init__(self, output_dir):
        if not os.path.isabs(output_dir):
            self.output_dir = os.path.join(os.path.dirname(__file__), '..', output_dir)
        log.msg("Will save pages to %s" % self.output_dir, log.INFO)
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            log.msg("Creating %s..." % self.output_dir, log.DEBUG)

    
    def process_item(self, item, spider):
        fname = os.path.join(self.output_dir, hashlib.sha224(item['url']).hexdigest())
        log.msg("Saving to file %s page with url %s" % (fname, item['url']), log.DEBUG)
        with open(fname, "wb") as resfile:
            resfile.write(item['content'])
        
