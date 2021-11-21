from kafka import KafkaProducer

TOPIC_NAME = 'items'
KAFKA_SERVER = 'kafka-0.kafka-headless.default.svc.cluster.local:9092'
# KAFKA_SERVER = 'localhost:9092'

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

producer.send(TOPIC_NAME, b'Hello re')
producer.flush()
