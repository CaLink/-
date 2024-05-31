import json
import scrapy
from ..items import CarCategoryItem, CarItem
from ..lib import save_car

class DongSpider(scrapy.Spider):
    name = "dong"
    allowed_domains = ["www.dongchedi.com"]

    main_url = 'https://www.dongchedi.com/motor/pc/car/brand/select_series_v2?limit={limit}&page=1'
    car_info_url = 'https://www.dongchedi.com/auto/params-carIds-{car_id}'
    custom_settings = {"LOG_FILE":f"{name}.log", 'FEED_EXPORT_ENCODING':'utf-8', 'DOWNLOAD_DELAY':1, 'ROBOTSTXT_OBEY':False}

    def __init__(self):
        super(DongSpider, self).__init__()

    def start_requests(self):
        yield scrapy.Request(
            self.main_url.format(limit=1),
            method='POST',
            callback=self.parse_init
        )

   
    def parse_init(self, response):
        data = json.loads(response.text)
        cnt = data['data']['series_count']
        cnt = 2
        yield scrapy.Request(
            self.main_url.format(limit=cnt),
            method='POST',
            callback=self.catalog_parse
        )

    def catalog_parse(self, response):
        data = json.loads(response.text)

        # for car_data in data['data']['series']:
        #     car = CarCategoryItem()

        #     car['id'] = car_data['id']
        #     car['isNew'] = car_data['new_car_tag']
        #     car['brand_name'] = car_data['brand_name']
        #     car['outter_name'] =  car_data['outter_name']
        #     car['cover'] = car_data['cover_url']
        #     car['car_list'] = ';'.join(str(x) for x in car_data['car_ids'])
        #     if car_data['has_dealer_price'] == True:
        #         car['dealer_price'] = car_data['dealer_price']
        #     if car_data['has_official_price'] == True:
        #         car['official_price'] = car_data['official_price']
        #     if car_data['has_subsidy_price'] == True:
        #         car['subsidy_price'] = car_data['subsidy_price']

        #     #TODO: Механизм сохранения - нужен ли?

        for catalog_data in data['data']['series']:
            for offer in catalog_data['car_ids']:
                yield scrapy.Request(
                    self.car_info_url.format(car_id=offer),
                    method='GET',
                    callback=self.offer_parser,
                    cb_kwargs={'id':offer}
                )

    def offer_parser(self, response, id):

        xpath_preset = '//div[@data-row-anchor="{tag}"]/div[2]/descendant::*/text()'

        car = CarItem()
        tag_list = car.fields.keys()
        for tag in tag_list:
            car[tag] = response.xpath(xpath_preset.format(tag=tag)).get()
        car['car_id'] = id

        save_car(car)

