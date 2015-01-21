name := "intro_to_spark"

version := "1.0"

scalaVersion := "2.10.4"

libraryDependencies += "org.apache.spark" %% "spark-core" % "1.2.0"

libraryDependencies += "com.datastax.spark" %% "spark-cassandra-connector" %  "1.1.0" withSources() withJavadoc()
