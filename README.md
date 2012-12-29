googler
=======

A utility for automated crawling of web-resources found using global search engines (like google, bing, yahoo etc.)

This is scrapy-based spider that:
* takes list of keywords;
* does search using GSE and keywords;
* crawles sites found.

Implemented:
* a number of search engines;
* filtration by MIME (using a list of regular expressions);
* search by queries from a list specified in settings.py
* restrict urls using regular expressions
* other minor features

Gonna implement:
* flexible architecture (to override crawling and storage logic);
* send requests through randomly selected proxies;
* clever content selection (check whether the downloaded page has the same topic as the etalon page(s) specified at startup).
