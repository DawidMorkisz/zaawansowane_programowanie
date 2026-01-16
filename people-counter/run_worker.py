import pika
import json
import time
import os

from api.storage import update_task
from worker.detector import detect_people


RABBIT_HOST = "rabbitmq"
QUEUE = "people_detection"

os.makedirs("processed", exist_ok=True)


def callback(ch, method, properties, body):
    task = json.loads(body)
    task_id = task["task_id"]
    image_path = task["image_path"]
    output = f"processed/{task_id}.jpg"

    try:
        update_task(task_id, status="processing")
        count = detect_people(image_path, output)
        update_task(
            task_id,
            status="done",
            people_count=count,
            output_image=output
        )
    except Exception:
        update_task(task_id, status="failed")

    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    while True:
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=RABBIT_HOST)
            )
            channel = connection.channel()
            channel.queue_declare(queue=QUEUE, durable=True)
            channel.basic_qos(prefetch_count=1)
            channel.basic_consume(queue=QUEUE, on_message_callback=callback)
            channel.start_consuming()
        except Exception:
            time.sleep(3)


if __name__ == "__main__":
    main()
