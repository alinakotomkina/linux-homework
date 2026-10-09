#!/usr/bin/python3
s=input()
t=input()
a=[]
for i in range(len(s)-len(t)+1):
    if s[i:i+len(t)]==t:
        a.append(i+1)
print(a)



