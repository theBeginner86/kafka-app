from kafka import KafkaConsumer
import logging


logging.basicConfig(level=logging.INFO)


class Consumer:

    def __init__(self):
        self._init_kafka_consumer()

    def _init_kafka_consumer(self):
        #self.kafka_host = "kafka.default.svc.cluster.local"
        self.kafka_host = "localhost:9092"
        self.kafka_topic = "testing"
        self.consumer = KafkaConsumer(
            "testing",
            bootstrap_servers=self.kafka_host,
            auto_offset_reset='earliest',
        )

    def consume_from_kafka(self):
        for message in self.consumer:
            logging.info(message.value)
            print(message.value.decode('utf-8'))


if __name__ == "__main__":

    consumer = Consumer()

    while True:
        consumer.consume_from_kafka()