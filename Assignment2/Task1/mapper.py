#!/usr/bin/env python3
import sys

for line in sys.stdin:	
		line = line.strip()
		if(not line.startswith('#')):
			try:
				x = line.split()
		
			except:     	
				continue
			print(x[0],x[1])
