import pyspark_cassandra
from pyspark_cassandra import CassandraSparkContext

from pyspark.sql import SQLContext
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from uuid import uuid1

import json

conf = SparkConf() \
    .setAppName("PySpark Cassandra Test") \
    .setMaster("spark://127.0.0.1:7077") \
    .set("spark.cassandra.connection.host", "127.0.0.1")

# set up our contexts
sc = CassandraSparkContext(conf=conf)
sql = SQLContext(sc)
stream = StreamingContext(sc, 1) # 1 second window

kafka_stream = KafkaUtils.createStream(stream, \
                                       "localhost:2181", \
                                       "raw-event-streaming-consumer",
                                        {"pageviews":1})

# (None, u'{"site_id": "02559c4f-ec20-4579-b2ca-72922a90d0df", "page": "/something.css"}')
parsed = kafka_stream.map(lambda (k, v): json.loads(v))

# aggregate page views by site
summed = parsed.map(lambda event: (event['site_id'], 1)).\
                reduceByKey(lambda x,y: x + y).\
                map(lambda x: {"site_id": x[0], "ts": str(uuid1()), "pageviews": x[1]})

summed.pprint()
summed.saveToCassandra("killranalytics", "real_time_data")

# send the results back through kafka
def push_aggregates_to_kafka(rdd):
    pass

summed.foreachRDD(push_aggregates_to_kafka)

stream.start()
stream.awaitTermination()

