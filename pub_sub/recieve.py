import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
channel = connection.channel()


channel.exchange_declare(exchange='logs', exchange_type='fanout')
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='logs', queue=queue_name)

print(' waiting for messages. To exit press ctrl+C')


def callback(ch, method, properties, body):
    print(' Received {}'.format(body.decode()))
    time.sleep(body.count(b'.'))
    print(' Done')


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()

