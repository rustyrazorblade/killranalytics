import org.apache.spark.{SparkContext,SparkConf}

import org.apache.spark.streaming.dstream.{ReceiverInputDStream, DStream}

import org.apache.spark.streaming.kafka.KafkaUtils

import org.apache.spark.streaming.{Seconds, StreamingContext}
import kafka.serializer.StringDecoder
import org.apache.spark.storage.StorageLevel

import com.datastax.spark.connector._

object RawEventProcessing {

  def main(args: Array[String]): Unit = {

    val conf = new SparkConf().setAppName("Simple Application").set("spark.cassandra.connection.host", "127.0.0.1")
    val sc = new SparkContext(conf)

    // kafka topic raw events will be published to
    val topic = "test"

    // setup streaming context - we want to be pushing data to the client asap
    val ssc = new StreamingContext(sc, Seconds(1))

    val kafkaParams: Map[String, String] = Map(
      "zookeeper.connect" -> "localhost:2181",
      "group.id" -> "consumer-spark",
      "auto.offset.reset" -> "smallest")

    /*
    my best understanding of the following code is as follows:

    createStream[] is a generic.  the stuff between [] is the typing
    the args that follow coorespond to this:

      streaming context
      kafka configuration params (see the map above)
      map of topic_name -> numPartitions to consume
      storageLevel: we're using in memory only because we're throwing away the data so quickly
     */

    val rawEvents: ReceiverInputDStream[(String, String)] = KafkaUtils.createStream[String, String, StringDecoder, StringDecoder](ssc, kafkaParams, Map(topic -> 1), StorageLevel.MEMORY_ONLY)

    rawEvents.print()

//    rawEvents.saveToCassandra("events", "customer_events")


    ssc.start()
    ssc.awaitTermination()

  }
}
