import pika
import json
import time

RABBIT_HOST = "rabbitmq"
QUEUE = "people_detection"


def get_channel():
    while True:
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=RABBIT_HOST)
            )
            channel = connection.channel()
            channel.queue_declare(queue=QUEUE, durable=True)
            return channel
        except Exception:
            time.sleep(2)


def publish_task(task: dict):
    channel = get_channel()
    channel.basic_publish(
        exchange="",
        routing_key=QUEUE,
        body=json.dumps(task),
        properties=pika.BasicProperties(delivery_mode=2)
    )
