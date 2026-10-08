#!/usr/bin/python3
n=int(input())
first=n//100
ser=(n//10)%10
posl=n%10
n=str(n)
print(first+ser+posl,', ',int(n[::-1]))




