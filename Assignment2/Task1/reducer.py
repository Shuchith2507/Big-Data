#!/usr/bin/env python3
import sys
prevWord=None
valueTotal=[]

file1 = open(sys.argv[1].strip(),"w")

for line in sys.stdin:
  (startnode,values)=line.split()
  value=int(values.strip())
  if prevWord==None:
    valueTotal.append(value)
    prevWord=startnode
    file1.write(startnode+",1"+"\n")
  elif(startnode==prevWord ):
    valueTotal.append(value)
  elif(startnode!=prevWord ):
    file1.write(startnode+",1"+"\n")
    print(f"{prevWord}\t{valueTotal}")
    valueTotal.clear()
    valueTotal.append(value)
    prevWord=startnode
print(f"{prevWord}\t{valueTotal}")

file1.close()
