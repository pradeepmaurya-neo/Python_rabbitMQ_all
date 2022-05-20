import pika
from pika.exchange_type import ExchangeType


connection_parameter = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameter)

channel = connection.channel()


channel.exchange_declare(exchange='acceptexchange', exchange_type=ExchangeType.fanout)

message = "Lets send this msg ..."

while True:
  channel.basic_publish(
    exchange='acceptexchange',
  routing_key='test',
    body = message,
    )

  print(f"Sent message {message}")
  input("Please Press any Key")

