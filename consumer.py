import pika

def recieved_message(ch, method, properties, body):
    print(f"Recieved Message {body}")

connection_para = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_para)

channel = connection.channel()

channel.queue_declare(queue='letterbox')

channel.basic_consume(queue='letterbox', auto_ack=True, on_message_callback=recieved_message)

print(f"Started consuming")

channel.start_consuming()


