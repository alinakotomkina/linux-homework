#!/usr/bin/python3
f=[]
with open('cds.fna','r') as file:
    for line in file:
        meta=line.strip()
        if meta[0]=='>':
            f.append({'metadata':meta[1:],'data': ''})

        else:
            f[-1]['data'] += meta
print(f)


