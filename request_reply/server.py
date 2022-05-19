import pika

def recieved_message(ch, method, properties, body):
    print(f"Request Recieved {properties.correlation_id}")
    ch.basic_publish('', routing_key=properties.reply_to, body=f"Hey its your Reply {properties.correlation_id}")

connection_para = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_para)

channel = connection.channel()

channel.queue_declare(queue='request_queue')

channel.basic_consume(queue='request_queue', auto_ack=True, on_message_callback=recieved_message)

print(f"Started Server")

channel.start_consuming()


