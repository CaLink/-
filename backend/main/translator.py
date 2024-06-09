import re
import sys, os

translator = {
    'sub_brand_name': {
        '华晨宝马':"BMW",
        '比亚迪':"BYD",
    },
    'official_price': {
        '万':1000,
    },
    'fuel_form': {
        '汽油':"бензин",
        '插电式混合动力':"подключаемый гибрид",
    },
    'engine_description': {
        '马力 ':"Л.С. ",
        '插电式混动':"подключаемый гибрид ",
    },
    'gearbox_description': {
        '挡手自一体':"ступенчатая автоматическая механическая коробка передач",
        'E-CVT无级变速':"Бесступенчатая трансмиссия E-CVT",
    },
}

def brand(typ, word):
    if word in translator[typ].keys():
        return translator[typ][word]
    else:
        return word

def price(typ, word):
    cost = float(''.join(re.findall(r'[0-9.]', word)))
    rank = translator[typ][''.join(re.findall(r'[^0-9.]', word))]

    return int(cost * rank)


def fuel(typ, word):
    if word in translator[typ].keys():
        return translator[typ][word]
    else:
        return word

def engine(typ, word):
    ans = word
    for key, value in translator[typ].items():
        ans = ans.replace(key, value)
    return ans

def gearbox(typ, word):
    ans = word
    for key, value in translator[typ].items():
       ans = ans.replace(key, value)
    return ans

methods = {
    'sub_brand_name': brand,
    'official_price': price,
    'fuel_form': fuel,
    'engine_description': engine,
    'gearbox_description': gearbox,
}


def translate(typ, word):
    try:
        if typ in translator.keys():
            method = methods[typ]
            ans = method(typ=typ, word=word)
            return ans
        else:
            return word
    except Exception as e:
        print(e)


