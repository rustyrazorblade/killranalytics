# killranalytics
Open source analytics platform powered by Apache Cassandra, Spark, and Kafka

# Building


# Running

To run the spark streaming job that runs the analytics:

```
cd spark
sbt assembly
spark-submit --master 'local[2]' --class RawEventProcessing target/scala-2.10/intro_to_spark-assembly-1.0.jar
```
