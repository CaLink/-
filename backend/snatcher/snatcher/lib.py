import requests
import json


def save_car(car):
    url = 'http://127.0.0.1:8000/car/'
    data = json.dumps(dict(car), ensure_ascii=False)
    response = requests.post(url, data=data)