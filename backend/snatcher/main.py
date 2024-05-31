from twisted.internet import reactor, defer
from .snatcher.spiders import dong
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging  

# Как бы прокинуть папку для логов
def main_func():
    configure_logging()
    
    # Готовим базовый конфиг
    parseConfig = CrawlerRunner(settings={'DOWNLOAD_DELAY':0,'ROBOTSTXT_OBEY':False})
    
    # Оборачиваем создание павуков в такую штуку
    # Потом нужно выполнить метод
    # Все такие штуки запустяться через reactor в конце
    # Я так и не научился их стопать
    @defer.inlineCallbacks
    def getUser():
        yield parseConfig.crawl(dong.DongSpider)
        reactor.stop()
    
    getUser()
    reactor.run()