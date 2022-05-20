import pika
from pika.exchange_type import ExchangeType


connection_parameter = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameter)

channel = connection.channel()


channel.exchange_declare(exchange='mainexchange', exchange_type=ExchangeType.direct)

message = "This message will expire...."

channel.basic_publish(
  exchange='mainexchange',
 routing_key='test',
  body = message,
  )

print(f"Sent message {message}")

connection.close()

