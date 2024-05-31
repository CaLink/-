# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CarCategoryItem(scrapy.Item):
    id = scrapy.Field()
    isNew = scrapy.Field()
    brand_name = scrapy.Field()
    outter_name = scrapy.Field()
    cover = scrapy.Field()
    car_list = scrapy.Field()
    dealer_price = scrapy.Field()
    official_price = scrapy.Field()
    subsidy_price = scrapy.Field()
    pass


class CarItem(scrapy.Item):
    car_id = scrapy.Field()
    sub_brand_name = scrapy.Field()
    official_price = scrapy.Field()
    fuel_form = scrapy.Field()
    market_time = scrapy.Field()
    engine_description = scrapy.Field()
    energy_elect_max_power = scrapy.Field()
    gearbox_description = scrapy.Field()
    pass