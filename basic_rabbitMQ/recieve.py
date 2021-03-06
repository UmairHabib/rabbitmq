
import pika,sys, os

def main():

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(b' [x] received ' + body)

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print('[x] waiting for messages. To exit press ctrl+c')
    channel.start_consuming()

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)

