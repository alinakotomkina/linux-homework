#!/usr/bin/python3
reference=input()
sample=input()
for i, referenc in enumerate(reference):
    if referenc!=sample[i]:
        print(i+1,':',referenc,'>',sample[i])


