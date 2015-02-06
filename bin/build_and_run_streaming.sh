#!/bin/sh

cd spark
sbt assembly && spark-submit --master 'local[2]' --class RawEventProcessing target/scala-2.10/killranalytics-assembly-1.0.jar

