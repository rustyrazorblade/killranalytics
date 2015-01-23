import org.apache.spark.{SparkContext,SparkConf}

import com.datastax.spark.connector._

object RawEventProcessing {
  def main(args: Array[String]): Unit = {

    val conf = new SparkConf().setAppName("Simple Application").set("spark.cassandra.connection.host", "127.0.0.1")
    val sc = new SparkContext(conf)
    val rdd = sc.cassandraTable("test", "words")

    rdd.collect().toList.foreach(println)

  }
}
