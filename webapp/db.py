from logging import getLogger

from cqlengine.connection import setup
from cqlengine.management import create_keyspace

# kafka
from kafka import KafkaClient, SimpleProducer, SimpleConsumer

logger = getLogger(__name__)


def connect_cassandra():
    # yay for hard coded....
    ks = "killranalytics"
    setup(["localhost"], ks)
    create_keyspace(ks, "SimpleStrategy", 1)

def connect_kafka():
    kafka = KafkaClient("localhost:9092")
    logger.info("Connected to kafka")
    return kafka
    # producer = SimpleProducer(kafka)

