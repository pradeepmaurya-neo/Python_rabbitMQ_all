import pika
connection_parameter = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameter)

channel = connection.channel()

channel.exchange_declare(exchange='simplehashing', exchange_type="x-consistent-hash")

routing_key="Hash me!"

message = "This is core Hashing msg"

channel.basic_publish(exchange='simplehashing',
 routing_key=routing_key, 
 body = message)

print(f"Sent message {message}")

connection.close()

