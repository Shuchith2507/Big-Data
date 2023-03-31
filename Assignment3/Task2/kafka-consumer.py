#!/usr/bin/env python3
from kafka import KafkaConsumer
from json import loads
from collections import defaultdict
import json
import sys
Topic_name= str(sys.argv[1])
consumer = KafkaConsumer(
    Topic_name,value_deserializer=lambda x: loads(x.decode('utf-8')))
x=[]
for message in consumer:
         k=message.value
         x.append(k)
         if(k[0]=='EOF'):
            break
x=x[:-1:]
x.sort()
y = defaultdict(list)
for j in range(len(x)):
    y[x[j][0]+'1'].append(float(x[j][6]))
    y[x[j][0]+'2'].append(float((x[j][7])))       
from statistics import mean
m = dict()
for k in y.keys():
    m[k]=round(mean(y[k]), 2)
y = dict()
for i,j in m.items():
    if(i[:-1:] not in y.keys()):
        y[i[:-1:]]={}
        
    if(i[-1]=='1'):
        y[i[:-1:]]['Min']=j
            
    elif(i[-1]=='2'):
        y[i[:-1:]]['Max']=j

json.dump(y, sys.stdout,indent=4)

