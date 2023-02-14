import requests


class API(object):
    def __init__(self):
        self.__product_type = ""
        self.__brand = ""
        self.__price = ""
        self.__rating = ""

    def set_params(self, param):
        print("we are in API class now")
        return param

    @staticmethod
    def send_api() -> str:
        response = requests.get("http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline").text
        parsed_response = ''
        return parsed_response
