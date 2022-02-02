import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
channel = connection.channel()


channel.queue_declare(queue='task_queue', durable=True)
print(' waiting for messages. To exit press ctrl+C')


def callback(ch, method, properties, body):
    print(' Received {}'.format(body.decode()))
    time.sleep(body.count(b'.'))
    print(' Done')
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()

