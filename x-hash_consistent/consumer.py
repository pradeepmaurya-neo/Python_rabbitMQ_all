import pika
from pika.exchange_type import ExchangeType

def recieved1_message(ch, method, properties, body):
    print(f"Queue 1: Recieved Message {body}")

def recieved2_message(ch, method, properties, body):
    print(f"Queue 2: Recieved Message {body}")

connection_para = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_para)

channel = connection.channel()

channel.exchange_declare(exchange='simplehashing', exchange_type="x-consistent-hash")

channel.queue_declare(queue='letterbox1')
channel.queue_bind('letterbox1', 'simplehashing', routing_key='1')
channel.basic_consume(queue='letterbox1', auto_ack=True, on_message_callback=recieved1_message)

channel.queue_declare(queue='letterbox2')
channel.queue_bind('letterbox2', 'simplehashing', routing_key='2')
channel.basic_consume(queue='letterbox2', auto_ack=True, on_message_callback=recieved2_message)

print(f"Started consuming")

channel.start_consuming()


