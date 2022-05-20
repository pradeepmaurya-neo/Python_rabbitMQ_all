import pika
from pika.exchange_type import ExchangeType

def dlx_recieved_message(ch, method, properties, body):
    print(f"dlx: Recieved Message {body}")


connection_para = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_para)

channel = connection.channel()


channel.queue_declare(queue='mainxchangequeue',
arguments={'x-dead-letter-exchange':'dlx', 'x-message-tt1':5000})
channel.queue_bind('mainxchangequeue', 'mainexchange', 'test')
channel.basic_consume(queue='mainxchangequeue', auto_ack=True, on_message_callback=dlx_recieved_message)


print(f"Started consuming dlx")

channel.start_consuming()


