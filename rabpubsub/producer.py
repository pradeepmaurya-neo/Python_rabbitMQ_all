import pika
from pika.exchange_type import ExchangeType
import time 
import random

con_para = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(con_para)

channel = connection.channel()

channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)

msg = "Message from Exchange test 1"

channel.basic_publish(exchange='pubsub', routing_key='', body=msg)

print(f"Sent message {msg}")

connection.close()

