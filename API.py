import requests
import json
import pandas as pd


class API(object):
    def __init__(self):
        self.lipstick_category_list = [
            "lipstick",
            "lip gloss",
            "liquid",
            "lip stain",
            "all"
        ]

        self.lipstick_tag_list = [
            "canadian",
            "natural",
            "gluten free",
            "non gmo",
            "peanut free product",
            "vegan",
            "cruelty free",
            "organic",
            "purpicks",
            "certclean",
            "chemical free",
            "ewg verified",
            "hypoallergenic",
            "no talc",
            "all"
        ]

        self.__product_type = ""
        self.__brand = ""
        self.__price = ""
        self.__rating = ""

    def check_request(self, TYPE, CATEGORY, TAG) -> tuple:
        if TYPE == "lipstick":
            CHECK_CATEGORY = True if CATEGORY in self.lipstick_category_list else False
            CHECK_TAG = True if TAG in self.lipstick_tag_list else False
        return CHECK_CATEGORY, CHECK_TAG

    @staticmethod
    def process_price(PRICE_RANGE):
        if PRICE_RANGE == "all":
            PROCESSED_PRICE_RANGE = "price_greater_than=0"
        elif PRICE_RANGE == "cheap":
            PROCESSED_PRICE_RANGE = "price_less_than=5"
        elif PRICE_RANGE == "middle":
            PROCESSED_PRICE_RANGE = "price_greater_than=5&price_less_than=15"
        elif PRICE_RANGE == "not expensive":
            PROCESSED_PRICE_RANGE = "price_less_than=10"
        elif PRICE_RANGE == "not cheap":
            PROCESSED_PRICE_RANGE = "price_greater_than=10"
        elif PRICE_RANGE == "expensive":
            PROCESSED_PRICE_RANGE = "price_greater_than=15"

        return PROCESSED_PRICE_RANGE

    def send_api(self, params) -> str:
        parsed_response = []

        BRAND = params["brand"]
        TYPE = params["type"]
        CATEGORY = params["category"]
        TAG = params["tag"]
        PRICE_RANGE = params["price_range"]

        PROCESSED_PRICE_RANGE = self.process_price(PRICE_RANGE=PRICE_RANGE)

        REQUEST = f"http://makeup-api.herokuapp.com/api/v1/products.json?" \
                  f"{PROCESSED_PRICE_RANGE}&brand={BRAND}&product_type={TYPE}&category={CATEGORY}&tag={TAG}"
        response = requests.get(REQUEST).text
        data = json.loads(response)

        CHECK_CATEGORY, CHECK_TAG = self.check_request(
            TYPE=TYPE,
            CATEGORY=CATEGORY,
            TAG=TAG
        )

        for el in data:
            parsed_response.append({
                "name": el['name'],
                "image_link": el["image_link"],
                "description": el["description"],
                "buttonText": f"purchase for {el['price']}",
                "product_link": el["product_link"],
            })

        res = {
            "parsed_response": parsed_response,
            "category": CHECK_CATEGORY,
            "tag": CHECK_TAG
        }

        return res
