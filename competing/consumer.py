import pika
import random
import time

def on_message_received(ch, method, properties, body):
    processing_time = random.randint(1, 6)
    print(f"Recieved message {body}, will take time {processing_time} to process")
    time.sleep(processing_time)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("Finished processing the message")


connection_para = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_para)

channel = connection.channel()

channel.queue_declare(queue='postbox')

channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='postbox', on_message_callback=on_message_received)

print("Start message consuming")

channel.start_consuming()