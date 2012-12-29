# -*- coding: UTF-8 -*-

SPIDER_MODULES = ['googler.spiders']
NEWSPIDER_MODULE = 'googler.spiders'
USER_AGENT = 'w3m/0.5.3+cvs-1.1055' 

DOWNLOADER_MIDDLEWARES = {
    'googler.downloader.FilteringDownloader': 500,
}

ITEM_PIPELINES = [
                  'googler.pipelines.GooglerPipeline'
                  ]

LOG_ENABLED = True
LOG_FILE = 'googler.log'
LOG_LEVEL = 'INFO'

DOWNLOAD_DELAY = 0.25

PROXY_CHECK_TIMEOUT=5.0

GOOGLER_ALLOWED_MIME = [
                        r'text/html',
                        r'application/pdf',
                        ]

GOOGLER_QUERIES = [
                   'порнуха',
                   'жесткий трах смотреть онлайн бесплатно',
                   'лесби видео онлайн бесплатно',
                   'молоденькие видео онлайн бесплатно',
                   'бдсм смотреть',
                   ]
GOOGLER_PAGES_TO_GET_FROM_ENGINE = 10
GOOGLER_USE_ENGINES = [
                       'Google',
#                       'Yandex',
                       'Yahoo',
                       'Bing'
                       ]
GOOGLER_FORBID_URLS = [
                       r'www\.youtube\.com',
                       ]
GOOGLER_OUTPUT_DIRECTORY = 'results' # either absolute or relative to googler's top directory

DEPTH_LIMIT = 20 # for each found site