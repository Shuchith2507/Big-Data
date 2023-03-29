#!/usr/bin/env python3
import sys
prevWord=""
valueTotal=0
for line in sys.stdin:
  (word,values)=line.split(' ')
  value=int(values.strip())
  if word==prevWord or prevWord=='':
    valueTotal=valueTotal+value
    prevWord=word
  else:
    print(prevWord,valueTotal)
    prevWord=word
    valueTotal=value
print(prevWord,valueTotal)
