# Purpose: Produces products, streaming sales transactions, and restocking activities to Kafka topics
# Author:  Gary A. Stafford
# Date: 2022-08-29
# Instructions: Modify the configuration.ini file to meet your requirements.

# Please install confluent-kafka package if it's not present in your local dev env yet
# python3 -m pip install confluent-kafka
import configparser
import json
import random
import time

from uuid import uuid4
from enum import Enum
from csv import reader
from datetime import datetime

from confluent_kafka import Producer
from confluent_kafka.serialization import StringSerializer, SerializationContext, MessageField
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer

from config.kafka import get_configs
from models.Product import Product
from models.Purchase import Purchase
from models.Inventory import Inventory

config = configparser.ConfigParser()
config.read("configuration/configuration.ini")

# *** CONFIGURATION ***
topic_products = config["KAFKA"]["topic_products"]
topic_purchases = config["KAFKA"]["topic_purchases"]
topic_inventories = config["KAFKA"]["topic_inventories"]

producer_conf = {"bootstrap.servers": config["KAFKA"]["bootstrap_servers"]}
schema_registry_conf = {'url': config["KAFKA"]["schema_registry_url"]}
schema_registry_client = SchemaRegistryClient(schema_registry_conf)
string_serializer = StringSerializer('utf_8')

min_sale_freq = int(config["SALES"]["min_sale_freq"])
max_sale_freq = int(config["SALES"]["max_sale_freq"])
number_of_sales = int(config["SALES"]["number_of_sales"])
transaction_quantity_one_item_freq = int(
    config["SALES"]["transaction_quantity_one_item_freq"]
)
item_quantity_one_freq = int(config["SALES"]["item_quantity_one_freq"])
member_freq = int(config["SALES"]["member_freq"])
club_member_discount = float(config["SALES"]["club_member_discount"])
add_supp_freq_group1 = int(config["SALES"]["add_supp_freq_group1"])
add_supp_freq_group2 = int(config["SALES"]["add_supp_freq_group2"])
supplements_cost = float(config["SALES"]["supplements_cost"])

min_inventory = int(config["INVENTORY"]["min_inventory"])
restock_amount = int(config["INVENTORY"]["restock_amount"])

# *** VARIABLES ***
products = []
propensity_to_buy_range = []

class MessageType(Enum):
    PRODUCT = 'Product'
    PURCHASE = 'Purchase'
    INVENTORY = 'Inventory'

def main():
    create_product_list()
    generate_sales()

def getAvroSerializer(messageType: MessageType, message) -> AvroSerializer:
    if messageType == MessageType.PRODUCT:
        avroSchemaFile = 'avro/Product.avsc'
        to_dict = product_to_dict
    elif messageType == MessageType.PURCHASE:
        avroSchemaFile = 'avro/Purchase.avsc'
        to_dict = purchase_to_dict
    elif messageType == MessageType.INVENTORY:
        avroSchemaFile = 'avro/Inventory.avsc'
        to_dict = inventory_to_dict

    with open(avroSchemaFile) as f:
        schema_str = f.read()
#         print("schema string: {0}", schema_str)

    avro_serializer = AvroSerializer(schema_registry_client, schema_str, to_dict)
    print("avro_serializer: {0}", avro_serializer)
    return avro_serializer

def product_to_dict(product, ctx):
    """
    Returns a dict representation of a Product instance for serialization.

    Args:
        product (Product): Product instance.

        ctx (SerializationContext): Metadata pertaining to the serialization
            operation.

    Returns:
        dict: Dict populated with product attributes to be serialized.
    """

    # User._address must not be serialized; omit from dict
#     print("Type of product")
    return product

def purchase_to_dict(purchase, ctx):
    """
    Returns a dict representation of a Purchase instance for serialization.

    Args:
        purchase (Purchase): Purchase instance.

        ctx (SerializationContext): Metadata pertaining to the serialization
            operation.

    Returns:
        dict: Dict populated with purchase attributes to be serialized.
    """

    return purchase

def inventory_to_dict(inventory, ctx):
    """
    Returns a dict representation of a Purchase instance for serialization.

    Args:
        purchase (Purchase): Purchase instance.

        ctx (SerializationContext): Metadata pertaining to the serialization
            operation.

    Returns:
        dict: Dict populated with purchase attributes to be serialized.
    """

    return inventory

# create products and propensity_to_buy lists from CSV data file
def create_product_list():
    with open("data/products.csv", "r") as csv_file:
        next(csv_file)  # skip header row
        csv_reader = reader(csv_file)
        csv_products = list(csv_reader)

    for p in csv_products:
        new_product = dict([
            ('transactionTime', str(datetime.utcnow())),
            ('productId', p[0]),
            ('category', p[1]),
            ('item', p[2]),
            ('size', p[3]),
            ('cogs', float(p[4])),
            ('price', float(p[5])),
            ('inventoryLevel', int(p[6])),
            ('containsFruit', to_bool(p[7])),
            ('containsVeggies', to_bool(p[8])),
            ('containsNuts', to_bool(p[9])),
            ('containsCaffeine', to_bool(p[10])),
            ('propensityToBuy', int(p[14]))
        ])
        products.append(new_product)
        publish_to_kafka(topic_products, MessageType.PRODUCT, new_product)
        propensity_to_buy_range.append(int(p[14]))
    propensity_to_buy_range.sort()


# generate synthetic sale transactions
def generate_sales():
    # common to all transactions
    range_min = propensity_to_buy_range[0]
    range_max = propensity_to_buy_range[-1]
    for x in range(0, number_of_sales):
        # common for each transaction's line items
        transaction_time = str(datetime.utcnow())
        is_member = random_club_member()
        member_discount = club_member_discount if is_member else 0.00

        # reset values
        rnd_propensity_to_buy = -1
        previous_rnd_propensity_to_buy = -1

        for y in range(0, random_transaction_item_quantity()):
            # reduces but not eliminates risk of duplicate products in same transaction - TODO: improve this method
            if rnd_propensity_to_buy == previous_rnd_propensity_to_buy:
                rnd_propensity_to_buy = closest_product_match(
                    propensity_to_buy_range, random.randint(range_min, range_max)
                )
            previous_rnd_propensity_to_buy = rnd_propensity_to_buy
            quantity = random_quantity()
            for p in products:
                if p.get('propensityToBuy') == rnd_propensity_to_buy:
                    add_supplement = random_add_supplements(p.get('productId'))
                    supplement_price = supplements_cost if add_supplement else 0.00
                    new_purchase = dict([
                        ('transactionTime', transaction_time),
                        ('transactionId', str(abs(hash(transaction_time)))),
                        ('productId', p.get('productId')),
                        ('price', p.get('price')),
                        ('quantity', random_quantity()),
                        ('isMember', is_member),
                        ('memberDiscount', member_discount),
                        ('addSupplements', add_supplement),
                        ('supplementPrice', supplement_price),
                        ('totalPurchase', 0)
                    ])
                    publish_to_kafka(topic_purchases, MessageType.PURCHASE, new_purchase)
                    inventoryLevel = p.get('inventoryLevel')
                    inventoryLevel = inventoryLevel - quantity
                    if inventoryLevel <= min_inventory:
                        restock_item(p.get('productId'))
                    break
        time.sleep(random.randint(min_sale_freq, max_sale_freq))


# restock inventories
def restock_item(product_id):
    for p in products:
        if p.get('productId') == product_id:
            inventoryLevel = p.get('inventoryLevel')
            new_level = inventoryLevel + restock_amount
            new_inventory = dict(
                ('eventTime', str(datetime.utcnow())),
                ('productId', p.get('productId')),
                ('existingLevel', p.get('inventoryLevel')),
                ('stockQuantity', restock_amount),
                ('newLevel', new_level)
            )
            p['inventoryLevel'] = new_level  # update existing product item
            publish_to_kafka(topic_inventories, MessageType.INVENTORY, new_inventory)
            break


# serialize object to json and publish message to kafka topic
def publish_to_kafka(topic, messageType, message):
    configs = get_configs()
    avro_serializer = getAvroSerializer(messageType, message)
    producer = Producer({'bootstrap.servers': 'localhost:9092'})

    print("producer is created")
    print("The message to be sent: {0}", message)
    producer.poll(0.0)
    try:
        producer.produce(topic=topic,
                        key=string_serializer(str(uuid4())),
                        value=avro_serializer(message, SerializationContext(topic, MessageField.VALUE)),
                        on_delivery=delivery_report)
    except ValueError:
       print("Invalid input, discarding record ...")

#     print("\nFlushing records...")
    producer.flush() # execute callback for previous messages
    print("Topic: {0}, Value: {1}".format(topic, message))

def delivery_report(err, msg):
    """
    Reports the failure or success of a message delivery.

    Args:
        err (KafkaError): The error that occurred on None on success.

        msg (Message): The message that was produced or failed.

    Note:
        In the delivery report callback the Message.key() and Message.value()
        will be the binary format as encoded by any configured Serializers and
        not the same object that was passed to produce().
        If you wish to pass the original object(s) for key and value to delivery
        report callback we recommend a bound callback or lambda where you pass
        the objects along.
    """

    if err is not None:
        print("Delivery failed for User record {}: {}".format(msg.key(), err))
        return
    print('User record {} successfully produced to {} [{}] at offset {}'.format(
        msg.key(), msg.topic(), msg.partition(), msg.offset()))

# convert uppercase boolean values from CSV file to Python
def to_bool(value):
    if type(value) == str and str(value).lower() == "true":
        return True
    return False


# find the closest match in propensity_to_buy_range range
# Credit: https://www.geeksforgeeks.org/python-find-closest-number-to-k-in-given-list/
def closest_product_match(lst, k):
    return lst[min(range(len(lst)), key=lambda i: abs(lst[i] - k))]


# individual item purchase quantity (usually 1, max 3)
def random_quantity():
    rnd = random.randint(1, 30)
    if rnd == 30:
        return 3
    if rnd <= item_quantity_one_freq:
        return 1
    return 2


# transaction items quantity (usually 1, max 3)
def random_transaction_item_quantity():
    rnd = random.randint(1, 20)
    if rnd >= 19:
        return 3
    if rnd <= transaction_quantity_one_item_freq:
        return 1
    return 2


# smoothie club membership? (usually False)
def random_club_member():
    rnd = random.randint(1, 10)
    if rnd <= member_freq:
        return True
    return False


# add supplements? (more frequently purchased for SF and SC products)
def random_add_supplements(product_id):
    rnd = random.randint(1, 10)
    if str(product_id).startswith("SF") or str(product_id).startswith("SC"):
        if rnd <= add_supp_freq_group1:
            return True
        return False
    if rnd <= add_supp_freq_group2:
        return True
    return False


if __name__ == "__main__":
    main()
