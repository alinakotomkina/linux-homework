#!/usr/bin/python3
s=input()
le=len(s)
fs=s[0]
ps=s[-1]
srs=s[len(s)//2]
ev=s[1::2]
pol=s==s[::-1]
print(le, fs, ps, srs, ev, s[::-1], pol)

