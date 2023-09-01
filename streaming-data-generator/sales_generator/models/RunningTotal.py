# -*- coding: utf-8 -*-

""" avro python class for file: RunningTotal """

import json
from helpers import default_json_serialize, todict
from typing import Union


class RunningTotal(object):

    schema = """
    {
        "type": "record",
        "name": "RunningTotal",
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
                "name": "transactions",
                "type": "int"
            },
            {
                "name": "quantities",
                "type": "int"
            },
            {
                "name": "sales",
                "type": "double"
            }
        ]
    }
    """

    def __init__(self, obj: Union[str, dict, 'RunningTotal']) -> None:
        if isinstance(obj, str):
            obj = json.loads(obj)

        elif isinstance(obj, type(self)):
            obj = obj.__dict__

        elif not isinstance(obj, dict):
            raise TypeError(
                f"{type(obj)} is not in ('str', 'dict', 'RunningTotal')"
            )

        self.set_eventTime(obj.get('eventTime', None))

        self.set_productId(obj.get('productId', None))

        self.set_transactions(obj.get('transactions', None))

        self.set_quantities(obj.get('quantities', None))

        self.set_sales(obj.get('sales', None))

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

    def set_transactions(self, value: int) -> None:

        if isinstance(value, int):
            self.transactions = value
        else:
            raise TypeError("field 'transactions' should be type int")

    def get_transactions(self) -> int:

        return self.transactions

    def set_quantities(self, value: int) -> None:

        if isinstance(value, int):
            self.quantities = value
        else:
            raise TypeError("field 'quantities' should be type int")

    def get_quantities(self) -> int:

        return self.quantities

    def set_sales(self, value: float) -> None:

        if isinstance(value, float):
            self.sales = value
        else:
            raise TypeError("field 'sales' should be type float")

    def get_sales(self) -> float:

        return self.sales

    def serialize(self) -> None:
        return json.dumps(self, default=default_json_serialize)
