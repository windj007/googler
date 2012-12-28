#!/bin/bash

[ -e googler.log ] && rm googler.log

scrapy crawl Googler
