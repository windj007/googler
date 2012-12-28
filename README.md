googler
=======

A utility for automated crawling of web-resources found using global search engines (like google, bing, yahoo etc.)

This is spider for scrapy that:
* takes list of keywords;
* does search using GSE and keywords;
* crawles sites found.

Gonna implement:
* flexible architecture (to override crawling and storage logic);
* send requests through randomly selected proxies;
* clever content selection (check whether the downloaded page has the same topic as the etalon page(s) specified at startup).
