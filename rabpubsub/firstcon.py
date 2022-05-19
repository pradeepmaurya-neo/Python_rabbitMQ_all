import pika
from pika.exchange_type import ExchangeType

conn_para = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(conn_para)

channel = connection.channel()

def on_receive(ch, method, properties, body):
    print(f"First Receiver: the received msg is {body}")

channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)

queue=channel.queue_declare(queue='', exclusive=True)
channel.queue_bind(exchange='pubsub', queue=queue.method.queue)

channel.basic_consume(queue=queue.method.queue, auto_ack=True, on_message_callback=on_receive)

print("start consuming...")
channel.start_consuming()
