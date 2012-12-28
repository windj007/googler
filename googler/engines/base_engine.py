import itertools

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
