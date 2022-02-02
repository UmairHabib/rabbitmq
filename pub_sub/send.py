import pika
import sys


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')  # durable used to restore lost messages

message = input('Enter Message  ')
channel.basic_publish(exchange='logs', routing_key='',
                      body=message.encode())  # persistent message storage, in case server failed to make it durable


print(' [x] message {}'.format(message))
connection.close()

