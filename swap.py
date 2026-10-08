#!/usr/bin/python3
a, b=map(int,input().split())
print(a,id(a),b,id(b))
a, b = b, a
print(a, id(a),b, id(b))


