#!/usr/bin/env python3
import pyspark
import sys
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local").appName("Assignment").getOrCreate()

df3 = spark.read.options(header='True', inferSchema='True', delimiter=',').csv(sys.argv[1])
df3 = df3.na.drop()
df3 = df3.dropDuplicates(['Ticket number'])
dt = df3.groupBy("RP State Plate").avg("Fine amount").collect()
dt1 = spark.createDataFrame(dt)
df4 = df3.filter(df3.Color == "WH")
df5 = df4.withColumnRenamed("RP State Plate","state").withColumnRenamed("Ticket number","ticket").withColumnRenamed("Fine amount","fine")
dt1 = dt1.withColumnRenamed("RP State Plate","avgstate").withColumnRenamed("avg(Fine amount)","avgfine")
df5.createOrReplaceTempView("assign1")
dt1.createOrReplaceTempView("avgtbl")
dfans = spark.sql("select ticket from assign1,avgtbl where avgstate=state AND avgfine<fine")
df4 = dfans.orderBy(["ticket"])

df4.coalesce(1).write.csv(sys.argv[2]) 
