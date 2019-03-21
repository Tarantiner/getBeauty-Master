# -*- coding: utf-8 -*-

###################################################################################
# scrapy configurations
BOT_NAME = 'getBeauty'
SPIDER_MODULES = ['getBeauty.spiders']
NEWSPIDER_MODULE = 'getBeauty.spiders'
ROBOTSTXT_OBEY = False
CONCURRENT_REQUESTS = 32
CONCURRENT_REQUESTS_PER_IP = 3
REDIRECT_ENABLED = False
RETRY_TIMES = 8
RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 403, 404, 407, 408]

###################################################################################
# distributed environment configuration
SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'
SCHEDULER_PERSIST = False
SCHEDULER_FLUSH_ON_START = True

###################################################################################
# db configurations
REDIS_URL = 'redis://name:password@ip:port'
MONGO_URI = 'localhost'
MONGO_DATABASE = 'beauty1'

###################################################################################
# middleware and pipeline
DOWNLOADER_MIDDLEWARES = {
    'getBeauty.middlewares.MyProxyMiddleWare': 542,
    'getBeauty.middlewares.MyUserAgentMiddleWare': 541,
}
ITEM_PIPELINES = {
    'getBeauty.pipelines.SaveImgpipeline': 300,
    'getBeauty.pipelines.SaveUrlpipeline': 500,
}

###################################################################################
# widget: whether test each proxy before crawling.
# if True, it cost much time when starting project, but more fluently when working,
# if False, it cost less time when starting project, but may less efficient when working.
# set True recommended
TEST_PROXY = True

