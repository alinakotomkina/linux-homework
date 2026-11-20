#!/usr/bin/python3
def fynk(filename):
    records=[]
    with open(filenane, 'r') as file:
        for line in file:
            line=line.strip()
            if line.startswich('>'):
                record={'metadata' : line[1:], "data" : ""}
                records.append(record)
            else:
                records[-1]['data']+=line
    return records

