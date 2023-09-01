# -*- coding: utf-8 -*-

""" avro python class for file: Inventory """

import json
from helpers import default_json_serialize, todict
from typing import Union


class Inventory(object):

    schema = """
    {
        "type": "record",
        "name": "Inventory",
        "namespace": "com.siemens.hps",
        "fields": [
            {
                "name": "eventTime",
                "type": "string"
            },
            {
                "name": "productId",
                "type": "string"
            },
            {
                "name": "existingLevel",
                "type": "int"
            },
            {
                "name": "stockQuantity",
                "type": "int"
            },
            {
                "name": "newLevel",
                "type": "int"
            }
        ]
    }
    """

    def __init__(self, obj: Union[str, dict, 'Inventory']) -> None:
        if isinstance(obj, str):
            obj = json.loads(obj)

        elif isinstance(obj, type(self)):
            obj = obj.__dict__

        elif not isinstance(obj, dict):
            raise TypeError(
                f"{type(obj)} is not in ('str', 'dict', 'Inventory')"
            )

        self.set_eventTime(obj.get('eventTime', None))

        self.set_productId(obj.get('productId', None))

        self.set_existingLevel(obj.get('existingLevel', None))

        self.set_stockQuantity(obj.get('stockQuantity', None))

        self.set_newLevel(obj.get('newLevel', None))

    def dict(self):
        return todict(self)

    def set_eventTime(self, value: str) -> None:

        if isinstance(value, str):
            self.eventTime = value
        else:
            raise TypeError("field 'eventTime' should be type str")

    def get_eventTime(self) -> str:

        return self.eventTime

    def set_productId(self, value: str) -> None:

        if isinstance(value, str):
            self.productId = value
        else:
            raise TypeError("field 'productId' should be type str")

    def get_productId(self) -> str:

        return self.productId

    def set_existingLevel(self, value: int) -> None:

        if isinstance(value, int):
            self.existingLevel = value
        else:
            raise TypeError("field 'existingLevel' should be type int")

    def get_existingLevel(self) -> int:

        return self.existingLevel

    def set_stockQuantity(self, value: int) -> None:

        if isinstance(value, int):
            self.stockQuantity = value
        else:
            raise TypeError("field 'stockQuantity' should be type int")

    def get_stockQuantity(self) -> int:

        return self.stockQuantity

    def set_newLevel(self, value: int) -> None:

        if isinstance(value, int):
            self.newLevel = value
        else:
            raise TypeError("field 'newLevel' should be type int")

    def get_newLevel(self) -> int:

        return self.newLevel

    def serialize(self) -> None:
        return json.dumps(self, default=default_json_serialize)
