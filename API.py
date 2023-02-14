import requests
import json
import pandas as pd


class API(object):
    def __init__(self):
        self.__product_type = ""
        self.__brand = ""
        self.__price = ""
        self.__rating = ""

    @staticmethod
    def send_api(params) -> str:
        title_list = []
        imageUrl_list = []
        text_list = []
        buttonText_list = []
        buttonUrl_list = []

        BRAND = params["brand"]
        TYPE = params["type"]
        PRICE_RANGE = params["cheap"]
        REQUEST = f"http://makeup-api.herokuapp.com/api/v1/products.json?brand={BRAND}&product_type={TYPE}"
        response = requests.get(REQUEST).text
        data = json.loads(response)  # string to json

        for el in data:
            title_list.append(el['name'])
            imageUrl_list.append(el["image_link"])
            text_list.append(el["description"])
            buttonText_list.append(f"purchase for {el['price']}")
            buttonUrl_list.append(el["product_link"])

        parsed_response = {
            "name": title_list,
            "image_link": imageUrl_list,
            "description": text_list,
            "buttonText": buttonText_list,
            "product_link": buttonUrl_list,
        }

        return parsed_response
