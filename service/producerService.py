import logging

from kafka import KafkaProducer
from config.config import Config


class Producer:
    def __init__(self):
        config = Config()
        self.producer = KafkaProducer(bootstrap_servers=[config.kafka_broker_url])

    def produce(self, topic, message):
        (self.producer
         .send(topic, message)
         .add_callback(self.on_send_success)
         .add_errback(self.on_send_error))

    def on_send_success(self, metadata):
        logging.info("message sent to topic: " + metadata.topic)

    def on_send_error(self, e):
        logging.error("error occurred sending message", exc_info=e)