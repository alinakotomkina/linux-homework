#!/usr/bin/python3
import sys
summ=float(sys.argv[1])
rate=float(sys.argv[2])
years=int(sys.argv[3])
total=summ*(1+rate/100)**years
print(f"{total:.2f}")


