import requests


class API(object):
    def __init__(self):
        self.__product_type = ""
        self.__brand = ""
        self.__price = ""
        self.__rating = ""

    @staticmethod
    def send_api(params) -> str:
        BRAND = params["brand"]
        TYPE = params["params"]
        response = requests.get(f"http://makeup-api.herokuapp.com/api/v1/products.json?brand={BRAND}&product_type={TYPE}").text
        print(response)
        parsed_response = ''
        return parsed_response
