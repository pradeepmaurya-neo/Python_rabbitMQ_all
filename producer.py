import pika

connection_parameter = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameter)

channel = connection.channel()

channel.queue_declare(queue='letterbox')

message = "This is message from rabbitMQ"

channel.basic_publish(exchange='', routing_key='letterbox', body = message)

print(f"Sent message {message}")

connection.close()

