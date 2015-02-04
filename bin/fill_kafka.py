from kafka import KafkaClient, SimpleProducer, SimpleConsumer

# To send messages synchronously
kafka = KafkaClient("localhost:9092")
producer = SimpleProducer(kafka)

import time
import json
from uuid import uuid4, uuid1
import random

# collect metrics for 10 sites
sites = [str(uuid4()) for x in range(10)]
for x in range(1000):

    message = {"site_id":       random.choice(sites),
               "pageview_id":   str(uuid1()) }

    producer.send_messages("pageviews", json.dumps(message))
    print message
    time.sleep(.2)
