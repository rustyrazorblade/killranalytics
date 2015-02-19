# killranalytics
Open source analytics platform powered by Apache Cassandra, Spark, and Kafka

# Building

You'll need a virtualenv.

For testing: `pip install -r requirements-dev.txt`

```
cd spark
sbt assembly
```

# Testing

`py.test`


# Running

To run the spark streaming job that runs the analytics:

```
cd spark
spark-submit --master 'local[2]' --class RawEventProcessing target/scala-2.10/killranalytics-assembly-1.0.jar
```

Note: if uwsgi install fails you may need to do:
```
sudo C_INCLUDE_PATH=/usr/local/include LIBRARY_PATH=/usr/local/lib pip install uwsgi
```
