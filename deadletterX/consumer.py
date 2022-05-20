import pika
from pika.exchange_type import ExchangeType

def dlx_recieved_message(ch, method, properties, body):
    print(f"dlx: Recieved Message {body}")


connection_para = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_para)

channel = connection.channel()

channel.exchange_declare(exchange='mainexchange', exchange_type=ExchangeType.direct)
channel.exchange_declare(
    exchange='dlx',
    exchange_type=ExchangeType.fanout,
)

channel.queue_declare(queue='mainxchangequeue',
arguments={'x-dead-letter-exchange':'dlx', 'x-message-tt1':5000})
channel.queue_bind('mainxchangequeue', 'mainexchange', 'test')
# channel.basic_consume(queue='mainxchangequeue', auto_ack=True, on_message_callback=dlx_recieved_message)

channel.queue_declare(queue='dlxqueue')
channel.queue_bind('dlxqueue', 'dlx')
channel.basic_consume(queue='dlxqueue', auto_ack=True, on_message_callback=dlx_recieved_message)

print(f"Started consuming dlx")

channel.start_consuming()


