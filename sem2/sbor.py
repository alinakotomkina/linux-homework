#!/usr/bin/python3
reads=['ATGCC','GCCAA','CAAAT','TTTGG']
k=int(input())
for i in range(len(reads)):
    for j in range(i+1,len(reads)):
        fir=reads[i]
        sec=reads[j]
        if fir[-k:]==sec[:k]:
            print(i+1,'-',j+1)

