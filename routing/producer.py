import pika
from pika.exchange_type import ExchangeType


con_para = pika.ConnectionParameters('localhost')

conn = pika.BlockingConnection(con_para)

channel = conn.channel()


channel.exchange_declare(exchange='mytopicexchange', exchange_type=ExchangeType.topic)

Received_payment_europeuser = "An European consumer paid for some thing"

channel.basic_publish(exchange='mytopicexchange', routing_key='user.europe.payments', body=Received_payment_europeuser)


print(f"sent message{Received_payment_europeuser}")

business_msg = "An European consumer Bussiness order"

channel.basic_publish(exchange='mytopicexchange', routing_key='bussiness.europe.order', body=business_msg)


print(f"sent message{business_msg}")

conn.close()

