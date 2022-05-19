import pika
from pika.exchange_type import ExchangeType

con_para = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(con_para)

channel = connection.channel()

def on_msg_rcv(ch, method, property, body):
    print(f"User service: Recieved new msg {body}")


channel.exchange_declare(exchange='mytopicexchange', exchange_type=ExchangeType.topic)

queue = channel.queue_declare(queue='', exclusive=True)

channel.queue_bind(queue=queue.method.queue, exchange='mytopicexchange', routing_key='user.#')


channel.basic_consume(queue=queue.method.queue, auto_ack=True, on_message_callback=on_msg_rcv)

print("Start consuming User")

channel.start_consuming()
