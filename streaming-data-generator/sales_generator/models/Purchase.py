# -*- coding: utf-8 -*-

""" avro python class for file: Purchase """

import json
from helpers import default_json_serialize, todict
from typing import Union


class Purchase(object):

    schema = """
    {
        "type": "record",
        "name": "Purchase",
        "namespace": "com.siemens.hps",
        "fields": [
            {
                "name": "transactionTime",
                "type": "string"
            },
            {
                "name": "transactionId",
                "type": "string"
            },
            {
                "name": "productId",
                "type": "string"
            },
            {
                "name": "price",
                "type": "double"
            },
            {
                "name": "quantity",
                "type": "int"
            },
            {
                "name": "isMember",
                "type": "boolean"
            },
            {
                "name": "memberDiscount",
                "type": "double"
            },
            {
                "name": "addSupplements",
                "type": "boolean"
            },
            {
                "name": "supplementPrice",
                "type": "double"
            },
            {
                "name": "totalPurchase",
                "type": "double"
            }
        ]
    }
    """

    def __init__(self, obj: Union[str, dict, 'Purchase']) -> None:
        if isinstance(obj, str):
            obj = json.loads(obj)

        elif isinstance(obj, type(self)):
            obj = obj.__dict__

        elif not isinstance(obj, dict):
            raise TypeError(
                f"{type(obj)} is not in ('str', 'dict', 'Purchase')"
            )

        self.set_transactionTime(obj.get('transactionTime', None))

        self.set_transactionId(obj.get('transactionId', None))

        self.set_productId(obj.get('productId', None))

        self.set_price(obj.get('price', None))

        self.set_quantity(obj.get('quantity', None))

        self.set_isMember(obj.get('isMember', None))

        self.set_memberDiscount(obj.get('memberDiscount', None))

        self.set_addSupplements(obj.get('addSupplements', None))

        self.set_supplementPrice(obj.get('supplementPrice', None))

        self.set_totalPurchase(obj.get('totalPurchase', None))

    def dict(self):
        return todict(self)

    def set_transactionTime(self, value: str) -> None:

        if isinstance(value, str):
            self.transactionTime = value
        else:
            raise TypeError("field 'transactionTime' should be type str")

    def get_transactionTime(self) -> str:

        return self.transactionTime

    def set_transactionId(self, value: str) -> None:

        if isinstance(value, str):
            self.transactionId = value
        else:
            raise TypeError("field 'transactionId' should be type str")

    def get_transactionId(self) -> str:

        return self.transactionId

    def set_productId(self, value: str) -> None:

        if isinstance(value, str):
            self.productId = value
        else:
            raise TypeError("field 'productId' should be type str")

    def get_productId(self) -> str:

        return self.productId

    def set_price(self, value: float) -> None:

        if isinstance(value, float):
            self.price = value
        else:
            raise TypeError("field 'price' should be type float")

    def get_price(self) -> float:

        return self.price

    def set_quantity(self, value: int) -> None:

        if isinstance(value, int):
            self.quantity = value
        else:
            raise TypeError("field 'quantity' should be type int")

    def get_quantity(self) -> int:

        return self.quantity

    def set_isMember(self, value: bool) -> None:

        if isinstance(value, bool):
            self.isMember = value
        else:
            raise TypeError("field 'isMember' should be type bool")

    def get_isMember(self) -> bool:

        return self.isMember

    def set_memberDiscount(self, value: float) -> None:

        if isinstance(value, float):
            self.memberDiscount = value
        else:
            raise TypeError("field 'memberDiscount' should be type float")

    def get_memberDiscount(self) -> float:

        return self.memberDiscount

    def set_addSupplements(self, value: bool) -> None:

        if isinstance(value, bool):
            self.addSupplements = value
        else:
            raise TypeError("field 'addSupplements' should be type bool")

    def get_addSupplements(self) -> bool:

        return self.addSupplements

    def set_supplementPrice(self, value: float) -> None:

        if isinstance(value, float):
            self.supplementPrice = value
        else:
            raise TypeError("field 'supplementPrice' should be type float")

    def get_supplementPrice(self) -> float:

        return self.supplementPrice

    def set_totalPurchase(self, value: float) -> None:

        if isinstance(value, float):
            self.totalPurchase = value
        else:
            raise TypeError("field 'totalPurchase' should be type float")

    def get_totalPurchase(self) -> float:

        return self.totalPurchase

    def serialize(self) -> None:
        return json.dumps(self, default=default_json_serialize)
