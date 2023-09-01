# -*- coding: utf-8 -*-

""" avro python class for file: PurchaseEnriched """

import json
from helpers import default_json_serialize, todict
from typing import Union


class PurchaseEnriched(object):

    schema = """
    {
        "type": "record",
        "name": "PurchaseEnriched",
        "namespace": "com.siemens.hps",
        "fields": [
            {
                "name": "transactionTime",
                "type": "string"
            },
            {
                "name": "transactionTimestamp",
                "type": "long"
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
                "name": "productCategory",
                "type": "string"
            },
            {
                "name": "productName",
                "type": "string"
            },
            {
                "name": "productSize",
                "type": "string"
            },
            {
                "name": "productCOGS",
                "type": "double"
            },
            {
                "name": "productPrice",
                "type": "double"
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
                "name": "purchasePrice",
                "type": "double"
            },
            {
                "name": "purchaseQuantity",
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

    def __init__(self, obj: Union[str, dict, 'PurchaseEnriched']) -> None:
        if isinstance(obj, str):
            obj = json.loads(obj)

        elif isinstance(obj, type(self)):
            obj = obj.__dict__

        elif not isinstance(obj, dict):
            raise TypeError(
                f"{type(obj)} is not in ('str', 'dict', 'PurchaseEnriched')"
            )

        self.set_transactionTime(obj.get('transactionTime', None))

        self.set_transactionTimestamp(obj.get('transactionTimestamp', None))

        self.set_transactionId(obj.get('transactionId', None))

        self.set_productId(obj.get('productId', None))

        self.set_productCategory(obj.get('productCategory', None))

        self.set_productName(obj.get('productName', None))

        self.set_productSize(obj.get('productSize', None))

        self.set_productCOGS(obj.get('productCOGS', None))

        self.set_productPrice(obj.get('productPrice', None))

        self.set_containsFruit(obj.get('containsFruit', None))

        self.set_containsVeggies(obj.get('containsVeggies', None))

        self.set_containsNuts(obj.get('containsNuts', None))

        self.set_containsCaffeine(obj.get('containsCaffeine', None))

        self.set_purchasePrice(obj.get('purchasePrice', None))

        self.set_purchaseQuantity(obj.get('purchaseQuantity', None))

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

    def set_transactionTimestamp(self, value: int) -> None:

        if isinstance(value, int):
            self.transactionTimestamp = value
        else:
            raise TypeError("field 'transactionTimestamp' should be type int")

    def get_transactionTimestamp(self) -> int:

        return self.transactionTimestamp

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

    def set_productCategory(self, value: str) -> None:

        if isinstance(value, str):
            self.productCategory = value
        else:
            raise TypeError("field 'productCategory' should be type str")

    def get_productCategory(self) -> str:

        return self.productCategory

    def set_productName(self, value: str) -> None:

        if isinstance(value, str):
            self.productName = value
        else:
            raise TypeError("field 'productName' should be type str")

    def get_productName(self) -> str:

        return self.productName

    def set_productSize(self, value: str) -> None:

        if isinstance(value, str):
            self.productSize = value
        else:
            raise TypeError("field 'productSize' should be type str")

    def get_productSize(self) -> str:

        return self.productSize

    def set_productCOGS(self, value: float) -> None:

        if isinstance(value, float):
            self.productCOGS = value
        else:
            raise TypeError("field 'productCOGS' should be type float")

    def get_productCOGS(self) -> float:

        return self.productCOGS

    def set_productPrice(self, value: float) -> None:

        if isinstance(value, float):
            self.productPrice = value
        else:
            raise TypeError("field 'productPrice' should be type float")

    def get_productPrice(self) -> float:

        return self.productPrice

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

    def set_purchasePrice(self, value: float) -> None:

        if isinstance(value, float):
            self.purchasePrice = value
        else:
            raise TypeError("field 'purchasePrice' should be type float")

    def get_purchasePrice(self) -> float:

        return self.purchasePrice

    def set_purchaseQuantity(self, value: int) -> None:

        if isinstance(value, int):
            self.purchaseQuantity = value
        else:
            raise TypeError("field 'purchaseQuantity' should be type int")

    def get_purchaseQuantity(self) -> int:

        return self.purchaseQuantity

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
