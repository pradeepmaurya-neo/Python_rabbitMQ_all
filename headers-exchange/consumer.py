import pika
from pika.exchange_type import ExchangeType

def recieved_message(ch, method, properties, body):
    print(f"Recieved Message {body}")

connection_para = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_para)

channel = connection.channel()

channel.exchange_declare(exchange='headersexchange', exchange_type=ExchangeType.headers)

channel.queue_declare(queue='letterbox')


bind_args = {
    'x-match': 'all',
    'name' : 'Pradeep',
    'age' : '31'

}

channel.queue_bind('letterbox', 'headersexchange', arguments=bind_args)


channel.basic_consume(queue='letterbox', auto_ack=True, on_message_callback=recieved_message)

print(f"Started consuming")

channel.start_consuming()


