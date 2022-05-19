import pika
from pika.exchange_type import ExchangeType
connection_parameter = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameter)

channel = connection.channel()

channel.queue_declare(queue='letterbox')

channel.exchange_declare(exchange='1stexchange', exchange_type=ExchangeType.direct)
channel.exchange_declare(exchange='2ndexchange', exchange_type=ExchangeType.fanout)

channel.exchange_bind('2ndexchange', '1stexchange')


message = "This is message gone through multiple exchange"

channel.basic_publish(exchange='1stexchange', routing_key='', body = message)

print(f"Sent message {message}")

connection.close()

