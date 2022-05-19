import pika
from pika.exchange_type import ExchangeType

def recieved_message(ch, method, properties, body):
    print(f"Recieved Message {body}")

connection_para = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_para)

channel = connection.channel()

channel.exchange_declare(exchange='2ndexchange', exchange_type=ExchangeType.fanout)

channel.queue_declare(queue='letterbox')

channel.basic_consume(queue='letterbox', auto_ack=True, on_message_callback=recieved_message)

channel.queue_bind('letterbox', '2ndexchange')

print(f"Started consuming")

channel.start_consuming()


