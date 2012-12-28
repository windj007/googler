SPIDER_MODULES = ['googler.spiders']
NEWSPIDER_MODULE = 'googler.spiders'
USER_AGENT = 'w3m/0.5.3+cvs-1.1055' 

ITEM_PIPELINES = [
                  'googler.pipelines.GooglerPipeline'
                  ]

LOG_ENABLED = True
LOG_FILE = 'googler.log'
LOG_LEVEL = 'INFO'

DOWNLOAD_DELAY = 0.25

PROXY_CHECK_TIMEOUT=5.0

GOOGLER_QUERIES = [
                   'rule-based systems'
                   ]
GOOGLER_PAGES_TO_GET_FROM_ENGINE = 5
GOOGLER_USE_ENGINES = [
                       'Google',
                       'Yandex',
                       'Yahoo',
                       'Bing'
                       ]
GOOGLER_OUTPUT_DIRECTORY = 'results' # either absolute or relative to googler's top directory

DEPTH_LIMIT = 5 # for each found site