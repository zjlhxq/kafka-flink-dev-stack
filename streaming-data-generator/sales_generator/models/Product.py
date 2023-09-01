# -*- coding: utf-8 -*-

""" avro python class for file: Product """

import json
from helpers import default_json_serialize, todict
from typing import Union


class Product(object):

    schema = """
    {
        "type": "record",
        "name": "Product",
        "namespace": "com.siemens.hps",
        "fields": [
            {
                "name": "transactionTime",
                "type": "string"
            },
            {
                "name": "productId",
                "type": "string"
            },
            {
                "name": "category",
                "type": "string"
            },
            {
                "name": "item",
                "type": "string"
            },
            {
                "name": "size",
                "type": "string"
            },
            {
                "name": "cogs",
                "type": "double"
            },
            {
                "name": "price",
                "type": "double"
            },
            {
                "name": "inventoryLevel",
                "type": "int"
            },
            {
                "name": "containsFruit",
                "type": "boolean"
            },
            {
                "name": "containsVeggies",
                "type": "boolean"
            },
            {
                "name": "containsNuts",
                "type": "boolean"
            },
            {
                "name": "containsCaffeine",
                "type": "boolean"
            },
            {
                "name": "propensityToBuy",
                "type": "int"
            }
        ]
    }
    """

    def __init__(self, obj: Union[str, dict, 'Product']) -> None:
        if isinstance(obj, str):
            obj = json.loads(obj)

        elif isinstance(obj, type(self)):
            obj = obj.__dict__

        elif not isinstance(obj, dict):
            raise TypeError(
                f"{type(obj)} is not in ('str', 'dict', 'Product')"
            )

        self.set_transactionTime(obj.get('transactionTime', None))

        self.set_productId(obj.get('productId', None))

        self.set_category(obj.get('category', None))

        self.set_item(obj.get('item', None))

        self.set_size(obj.get('size', None))

        self.set_cogs(obj.get('cogs', None))

        self.set_price(obj.get('price', None))

        self.set_inventoryLevel(obj.get('inventoryLevel', None))

        self.set_containsFruit(obj.get('containsFruit', None))

        self.set_containsVeggies(obj.get('containsVeggies', None))

        self.set_containsNuts(obj.get('containsNuts', None))

        self.set_containsCaffeine(obj.get('containsCaffeine', None))

        self.set_propensityToBuy(obj.get('propensityToBuy', None))

    def dict(self):
        return todict(self)

    def set_transactionTime(self, value: str) -> None:

        if isinstance(value, str):
            self.transactionTime = value
        else:
            raise TypeError("field 'transactionTime' should be type str")

    def get_transactionTime(self) -> str:

        return self.transactionTime

    def set_productId(self, value: str) -> None:

        if isinstance(value, str):
            self.productId = value
        else:
            raise TypeError("field 'productId' should be type str")

    def get_productId(self) -> str:

        return self.productId

    def set_category(self, value: str) -> None:

        if isinstance(value, str):
            self.category = value
        else:
            raise TypeError("field 'category' should be type str")

    def get_category(self) -> str:

        return self.category

    def set_item(self, value: str) -> None:

        if isinstance(value, str):
            self.item = value
        else:
            raise TypeError("field 'item' should be type str")

    def get_item(self) -> str:

        return self.item

    def set_size(self, value: str) -> None:

        if isinstance(value, str):
            self.size = value
        else:
            raise TypeError("field 'size' should be type str")

    def get_size(self) -> str:

        return self.size

    def set_cogs(self, value: float) -> None:

        if isinstance(value, float):
            self.cogs = value
        else:
            raise TypeError("field 'cogs' should be type float")

    def get_cogs(self) -> float:

        return self.cogs

    def set_price(self, value: float) -> None:

        if isinstance(value, float):
            self.price = value
        else:
            raise TypeError("field 'price' should be type float")

    def get_price(self) -> float:

        return self.price

    def set_inventoryLevel(self, value: int) -> None:

        if isinstance(value, int):
            self.inventoryLevel = value
        else:
            raise TypeError("field 'inventoryLevel' should be type int")

    def get_inventoryLevel(self) -> int:

        return self.inventoryLevel

    def set_containsFruit(self, value: bool) -> None:

        if isinstance(value, bool):
            self.containsFruit = value
        else:
            raise TypeError("field 'containsFruit' should be type bool")

    def get_containsFruit(self) -> bool:

        return self.containsFruit

    def set_containsVeggies(self, value: bool) -> None:

        if isinstance(value, bool):
            self.containsVeggies = value
        else:
            raise TypeError("field 'containsVeggies' should be type bool")

    def get_containsVeggies(self) -> bool:

        return self.containsVeggies

    def set_containsNuts(self, value: bool) -> None:

        if isinstance(value, bool):
            self.containsNuts = value
        else:
            raise TypeError("field 'containsNuts' should be type bool")

    def get_containsNuts(self) -> bool:

        return self.containsNuts

    def set_containsCaffeine(self, value: bool) -> None:

        if isinstance(value, bool):
            self.containsCaffeine = value
        else:
            raise TypeError("field 'containsCaffeine' should be type bool")

    def get_containsCaffeine(self) -> bool:

        return self.containsCaffeine

    def set_propensityToBuy(self, value: int) -> None:

        if isinstance(value, int):
            self.propensityToBuy = value
        else:
            raise TypeError("field 'propensityToBuy' should be type int")

    def get_propensityToBuy(self) -> int:

        return self.propensityToBuy

    def serialize(self) -> None:
        return json.dumps(self, default=default_json_serialize)
