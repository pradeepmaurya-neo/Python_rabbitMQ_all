import pika
from pika.exchange_type import ExchangeType


connection_parameter = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameter)

channel = connection.channel()

# channel.queue_declare(queue='letterbox')

channel.exchange_declare(exchange='headersexchange', exchange_type=ExchangeType.headers)



message = "This is message gone through Headers 2"

channel.basic_publish(exchange='headersexchange',
 routing_key='',
  body = message,
  properties=pika.BasicProperties(headers={
      'name': 'Pradeep'
  }),
  )

print(f"Sent message {message}")

connection.close()

