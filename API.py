import requests
import json
import pandas as pd


class API(object):
    def __init__(self):
        self.lipstick_category_list = ["lipstick", "lip gloss", "liquid", "lip stain", "all"
        ]

        self.lipstick_tag_list = ["canadian", "natural", "gluten free", "non gmo", "peanut free product", "vegan",
            "cruelty free", "organic", "purpicks", "certclean", "chemical free", "ewg verified", "hypoallergenic",
            "no talc", "all"
        ]

        self.blush_category_list = ["powder", "cream", "all"]

        self.blush_tag_list = ["Vegan", "Gluten free", "Canadian", "Natural", "Non-gmot", "Purpicks", "Usda organic",
            "Organic", "Certclean", "Ewg verified", "Hypoallergenic", "No talc",
        ]

        self.bronzer_category_list = ["powder", "all"]
        self.bronzer_tag_list = ["gluten_free", "canadian", "natural", "organic", "vegan", "purpicks", "ewg_verified", "all"]

        self.eyebrow_category_list = ["pencil", "all"]
        self.eyebrow_tag_list = ["Ewg verified", "Purpicks", "all"]

        self.eyeliner_category_list = ["Liquid", "Pencil", "Gel", "Cream", "all"]
        self.eyeliner_tag_list = ["Vegan", "Natural", "Canadian", "Gluten free", "Organic", "Purpicks", "Certclean",
                             "Ewg verified", "Hypoallergenic", "No talc", "Ecocert", "all"]

        self.eyeshadow_category_list = ["Palette", "Pencil", "Cream", "All"]
        self.eyeshadow_tag_list = ["Vegan", "Canadian", "Natural", "Gluten Free", "Non-GMO", "Purpicks", "CertClean",
                              "EWG Verified", "Organic", "USDA Organic", "Hypoallergenic", "No Talc", "EcoCert", "All"]

        self.foundation_category_list = ["Concealer", "Liquid", "Contour", "Bb cc", "Cream", "Mineral", "Powder",
                                         "Highlighter", "All"]
        self.foundation_tag_list = ["Vegan", "Canadian", "Natural", "Gluten Free", "Purpicks", "Certclean",
                                    "Ewg Verified", "Hypoallergenic", "No Talc", "Water Free", "Cruelty Free",
                                    "Alcohol Free", "Oil Free", "Silicone Free", "All"]

        self.lipliner_category_list = ["pencil", "all"]
        self.lipliner_tag_list = ["Natural", "Vegan", " Gluten free", "Canadian", "Purpicks", "Ewg verified",
                                  "Hypoallergenic", "No talc", "Cruelty free", "All"]

        self.mascara_category_list = ["all"]
        self.mascara_tag_list = ['Natural', 'Gluten Free', 'Vegan', 'Canadian', 'Organic', 'Purpicks', 'Ewg Verified',
                            'Hypoallergenic', 'No Talc', 'Ecocert', 'Usda Organic', 'Certclean', 'All']

        self.nailpolish_category_list = ["all"]
        self.nailpolish_tag_list = ["Vegan", "Canadian", "Natural", "Gluten free", "Fair trade", "Sugar free",
                                    "Non-gmo", "Dairy free", "All"]

        self.__product_type = ""
        self.__brand = ""
        self.__price = ""
        self.__rating = ""

    def check_request(self, TYPE, CATEGORY, TAG) -> tuple:
        if TYPE == "lipstick":
            CHECK_CATEGORY = True if CATEGORY in self.lipstick_category_list else False
            CHECK_TAG = True if TAG in self.lipstick_tag_list else False

        # Blush
        if TYPE == "blush":
            CHECK_CATEGORY = True if CATEGORY in self.blush_category_list else False
            CHECK_TAG = True if TAG in self.blush_tag_list else False

        # Bronzer
        if TYPE == "bronzer":
            CHECK_CATEGORY = True if CATEGORY in self.bronzer_category_list else False
            CHECK_TAG = True if TAG in self.bronzer_tag_list else False

        # Eyebrow
        if TYPE == "eyebrow":
            CHECK_CATEGORY = True if CATEGORY in self.eyebrow_category_list else False
            CHECK_TAG = True if TAG in self.eyebrow_tag_list else False

        # Eyeliner
        if TYPE == "eyeliner":
            CHECK_CATEGORY = True if CATEGORY in self.eyeliner_category_list else False
            CHECK_TAG = True if TAG in self.eyeliner_tag_list else False

        # Eyeshadow
        if TYPE == "eyeshadow":
            CHECK_CATEGORY = True if CATEGORY in self.eyeshadow_category_list else False
            CHECK_TAG = True if TAG in self.eyeshadow_tag_list else False

        # Foundation
        if TYPE == "foundation":
            CHECK_CATEGORY = True if CATEGORY in self.foundation_category_list else False
            CHECK_TAG = True if TAG in self.foundation_tag_list else False

        # Lipliner
        if TYPE == "lipliner":
            CHECK_CATEGORY = True if CATEGORY in self.lipliner_category_list else False
            CHECK_TAG = True if TAG in self.lipliner_tag_list else False

        # Mascara
        if TYPE == "mascara":
            CHECK_CATEGORY = True if CATEGORY in self.mascara_category_list else False
            CHECK_TAG = True if TAG in self.mascara_tag_list else False

        # Nailpolish
        if TYPE == "nailpolish":
            CHECK_CATEGORY = True if CATEGORY in self.nailpolish_category_list else False
            CHECK_TAG = True if TAG in self.nailpolish_tag_list else False

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
