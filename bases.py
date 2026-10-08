#!/usr/bin/python3
import sys
num=int(sys.argv[1])
bi=bin(num)[2:]
oc=oct(num)[2:]
he=hex(num)[2:]
print(bi, oc, he)
n=int(str(bi),2)
print(n)

