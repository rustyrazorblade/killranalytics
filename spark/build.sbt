import AssemblyKeys._

assemblySettings

name := "killranalytics"

version := "1.0"

scalaVersion := "2.10.4"

libraryDependencies += "org.apache.spark" %% "spark-core" % "1.2.1" % "provided"

libraryDependencies += "com.datastax.spark" %% "spark-cassandra-connector" %  "1.2.0-alpha2"

libraryDependencies += "org.apache.spark" %% "spark-streaming" % "1.2.1" % "provided"

libraryDependencies += "org.apache.spark" %% "spark-streaming-kafka" % "1.2.1"

val json4sVersion = "3.2.10"

libraryDependencies += "org.json4s" %% "json4s-native" % json4sVersion

libraryDependencies += "org.json4s" %% "json4s-jackson" % json4sVersion

libraryDependencies += "org.json4s" %% "json4s-ext" % json4sVersion

