#!/usr/bin/env python3
import sys
import math
import json

for line in sys.stdin:	
		line = json.loads(line.strip())
		try:
			if((line["location"]>1700 and line["location"]<2500) and line["sensor_id"]<5000 and line["pressure"]>= 93500.00 and line["humidity"]>= 72.00 and line["temperature"]>= 12.00):
				print(line['timestamp'],1)
		except:     	
			continue
