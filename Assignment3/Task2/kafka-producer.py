#!/usr/bin/env python3
from kafka import KafkaProducer
from json import dumps
import sys
topic_name= str(sys.argv[1])
KAFKA_SERVER = 'localhost:9092'
x = []
import csv

data = sys.stdin.readlines()

for line in csv.reader(data):

     x.append(line)
producer=KafkaProducer(bootstrap_servers=KAFKA_SERVER,value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
                         
for i in x:
        producer.send(topic_name,value=i)
        producer.flush()

