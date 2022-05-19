import pika
import time
import random

connection_para = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_para)

channel = connection.channel()

channel.queue_declare(queue='postbox')

mesgeID =1

while True:

    message = f"This rabbitMQ MSG {mesgeID}"

    channel.basic_publish(exchange='', routing_key='postbox', body=message)

    print(f"Sent message to consumer {message}")

    time.sleep(random.randint(1, 4))

    mesgeID +=1

    # connection.close()
