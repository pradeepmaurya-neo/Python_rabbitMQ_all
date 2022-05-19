import pika
import uuid


con_para = pika.ConnectionParameters('localhost')

conn = pika.BlockingConnection(con_para)

channel = conn.channel()

def on_reply_msg(ch, method, properties, body):
    print(f"Reply Recieved :{body}")

reply_queue=channel.queue_declare(queue='', exclusive=True)

channel.basic_consume(queue=reply_queue.method.queue, auto_ack=True, on_message_callback=on_reply_msg)

msg = "Can I request a reply"
channel.queue_declare(queue='request_queue')

cor_id = str(uuid.uuid4())
print(f"sendind Request: {cor_id}")

channel.basic_publish(
    exchange='',
    routing_key='request_queue',
    body=msg,
    properties=pika.BasicProperties(
        reply_to=reply_queue.method.queue,
        correlation_id=cor_id,)
    )

print(f"Start Client")


channel.start_consuming()
