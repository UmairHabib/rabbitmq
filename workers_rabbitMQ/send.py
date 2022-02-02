import pika
import sys


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)  # durable used to restore lost messages

message = input('Enter Message  ')
channel.basic_publish(exchange='', routing_key='task_queue',
                      body=message.encode(), properties=pika.BasicProperties(
                      delivery_mode=2,))  # persistent message storage, in case server failed to make it durable


print(' [x] message {}'.format(message))
connection.close()

