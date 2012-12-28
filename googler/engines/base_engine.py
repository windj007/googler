import itertools

class BaseEngine(object):
    def get_result_extractors(self):
        return []

    def get_start_pages(self, queries, num_of_pages):
        return itertools.chain(self.make_pages_for_query(query, num_of_pages) for query in queries)
    
    def make_pages_for_query(self, query, num_of_pages):
        return []
