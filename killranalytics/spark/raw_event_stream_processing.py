import pyspark_cassandra
from pyspark_cassandra import CassandraSparkContext

from pyspark.sql import SQLContext
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

import json

conf = SparkConf() \
    .setAppName("PySpark Cassandra Test") \
    .setMaster("spark://127.0.0.1:7077") \
    .set("spark.cassandra.connection.host", "127.0.0.1")

# set up our contexts
sc = CassandraSparkContext(conf=conf)
sql = SQLContext(sc)
stream = StreamingContext(sc, 1) # 1 second window

topic = "pageviews"

kafka_stream = KafkaUtils.createStream(stream, \
                                       "localhost:2181", \
                                       "raw-event-streaming-consumer",
                                        {topic:1})

kafka_stream.pprint()

# (None, u'{"site_id": "02559c4f-ec20-4579-b2ca-72922a90d0df", "page": "/something.css"}')
parsed = kafka_stream.map(lambda (k, v): json.loads(v))

# aggregate page views by site
summed = parsed.map(lambda event: (event['site_id'], 1)).reduceByKey(lambda x,y: x + y)
summed.pprint()

stream.start()
stream.awaitTermination()

