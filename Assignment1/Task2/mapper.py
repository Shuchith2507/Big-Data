#!/usr/bin/env python3
import sys
import math
import json

acc_lat = float(sys.argv[2])
acc_lon = float(sys.argv[3])
D = int(sys.argv[1])

for line in sys.stdin:	
		line = json.loads(line.strip())
		try:
			if(( 48.0 < line["humidity"]<54.0) and (20.0 < line["temperature"]<24.0)): 
				dist = math.sqrt(pow((acc_lat - line["lat"]),2) + pow((acc_lon - line["lon"]),2))
				if(D>dist):
					print(line['timestamp'],1)
		except:     	
			continue
