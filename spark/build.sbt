import AssemblyKeys._

assemblySettings

name := "killranalytics"

version := "1.0"

scalaVersion := "2.10.4"

libraryDependencies += "org.apache.spark" %% "spark-core" % "1.2.0" % "provided"

libraryDependencies += "com.datastax.spark" %% "spark-cassandra-connector" %  "1.2.0-alpha1" withSources() withJavadoc()

libraryDependencies += "org.apache.spark" %% "spark-streaming" % "1.2.0" % "provided"

libraryDependencies += "org.apache.spark" %% "spark-streaming-kafka" % "1.2.0"

